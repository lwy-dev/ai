from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

# 认证Token
VALID_TOKEN = "lwy"

# 城市经纬度
CITYS = {
    "北京": (39.9042, 116.4074),
    "上海": (31.2304, 121.4737),
    "广州": (23.1291, 113.2644),
    "深圳": (22.5431, 114.0579),
    "杭州": (30.2741, 120.1551),
    "成都": (30.5728, 104.0668),
    "武汉": (30.5928, 114.3055),
    "西安": (34.3416, 108.9398),
    "南京": (32.0603, 118.7969),
    "重庆": (29.5630, 106.5516)
}


class WeatherRequest(BaseModel):
    location: str


def weather_code_to_text(code):
    mapping = {
        0: "晴天",
        1: "基本晴",
        2: "局部多云",
        3: "阴天",
        45: "雾",
        48: "冻雾",
        51: "小毛毛雨",
        53: "毛毛雨",
        55: "大毛毛雨",
        61: "小雨",
        63: "中雨",
        65: "大雨",
        71: "小雪",
        73: "中雪",
        75: "大雪",
        80: "阵雨",
        81: "较强阵雨",
        82: "暴雨",
        95: "雷暴"
    }
    return mapping.get(code, "未知天气")


@app.post("/weather")
def get_weather(request: Request, body: WeatherRequest):

    # Token验证
    auth = request.headers.get("Authorization")

    if auth != f"Bearer {VALID_TOKEN}":
        raise HTTPException(
            status_code=403,
            detail="Invalid Authorization header"
        )

    city = body.location

    if city not in CITYS:
        return {
            "status": "error",
            "message": f"暂不支持城市：{city}"
        }

    lat, lon = CITYS[city]

    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}"
        f"&longitude={lon}"
        f"&current=temperature_2m,weather_code"
    )

    try:
        r = requests.get(
            url,
            timeout=15,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        r.raise_for_status()

        data = r.json()

        current = data["current"]

        temp = current["temperature_2m"]
        code = current["weather_code"]

        weather_text = weather_code_to_text(code)

        return {
            "status": "success",
            "weather": f"{city}当前天气：{weather_text}，气温 {temp}°C"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8081
    )