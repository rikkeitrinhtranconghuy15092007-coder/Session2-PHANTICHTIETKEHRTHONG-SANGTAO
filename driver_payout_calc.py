# RikkeiExpress - Template tính toán hoa hồng tài xế
def calculate_payout(trips_completed, base_rate=15000, bonus_threshold=50):
    base_payout = trips_completed * base_rate
    bonus = 500000 if trips_completed > bonus_threshold else 0
    return base_payout + bonus

if __name__ == "__main__":
    print("Driver Payout (55 trips):", calculate_payout(55))
