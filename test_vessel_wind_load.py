# Import pytest and calculations file
import pytest as pt
import vessel_wind_load

# Defining Tests
def test_check_vessel_dimensions_zero(): # Case boat length zero
    with pt.raises(ValueError):
        vessel_wind_load.check_vessel_dimensions(0)

def test_check_vessel_dimensions_negative(): # Case boat length negative
    with pt.raises(ValueError):
        vessel_wind_load.check_vessel_dimensions(-5)

def test_check_vessel_dimensions_large(): # Case boat length > 300
    with pt.raises(ValueError):
        vessel_wind_load.check_vessel_dimensions(301)

# def test_check_vessel_dimensions_valid(): # Case valid boat length
#     with pt.raises(ValueError):
#         vessel_wind_load.check_vessel_dimensions(150)       


def test_check_shielding_factor_lower_bound(): # Case shielding factor too low
    with pt.raises(ValueError):
        vessel_wind_load.check_shielding_factor(0.29)

def test_check_shielding_factor_upper_bound(): # Case shielding factor too high
    with pt.raises(ValueError):
        vessel_wind_load.check_shielding_factor(1.01)

def test_check_direction_factor_lower_bound(): # Case direction factor too low
    with pt.raises(ValueError):
        vessel_wind_load.check_direction_factor(0.99)

def test_check_direction_factor_upper_bound(): # Case direction factor too high
    with pt.raises(ValueError):
        vessel_wind_load.check_direction_factor(3.6)


def test_calculate_vessel_beam(): # Check vessel beam against affirmed values, normal and upper end
    check_beam_low = 13.9
    check_beam_high = 44.9
    calc_beam_low = round(vessel_wind_load.calculate_vessel_beam(50), 1)
    calc_beam_high = round(vessel_wind_load.calculate_vessel_beam(200), 1)
    assert (check_beam_low == pt.approx(calc_beam_low))
    assert (check_beam_high == pt.approx(calc_beam_high))

def test_calculate_vessel_height(): # Check vessel height against affirmed values, normal and upper end
    check_height_low = 9.4
    check_height_high = 21.6
    calc_height_low = round(vessel_wind_load.calculate_vessel_height(50), 1)
    calc_height_high = round(vessel_wind_load.calculate_vessel_height(200), 1)
    assert (check_height_low == pt.approx(calc_height_low))
    assert (check_height_high == pt.approx(calc_height_high))

def test_calculate_vessel_draft(): # Check vessel draft against affirmed values, normal and upper end
    check_draft_low = 3.9
    check_draft_high = 12.2
    calc_draft_low = round(vessel_wind_load.calculate_vessel_draft(50), 1)
    calc_draft_high = round(vessel_wind_load.calculate_vessel_draft(200), 1)    
    assert (check_draft_low == pt.approx(calc_draft_low))
    assert (check_draft_high == pt.approx(calc_draft_high))

def test_calculate_end_area(): # Check vessel end area against affirmed values, normal and upper end
    check_area_low = 130.9
    check_area_high = 970.5
    calc_area_low = round(vessel_wind_load.calculate_end_area(50), 1)
    calc_area_high = round(vessel_wind_load.calculate_end_area(200), 1)
    assert (check_area_low == pt.approx(calc_area_low))
    assert (check_area_high == pt.approx(calc_area_high))

def test_calculate_wind_force(): # Check wind force calculation against affirmed value, with _____ tolerance
    check_force = 2.789
    calc_force = round(vessel_wind_load.calculate_wind_force(50, 3.5, 1.0, 45),3)
    assert(check_force == pt.approx(calc_force))


# Running Tests
test_check_vessel_dimensions_zero()
test_check_vessel_dimensions_negative()
test_check_vessel_dimensions_large()
# test_check_vessel_dimensions_valid()

test_check_shielding_factor_lower_bound()
test_check_shielding_factor_upper_bound()

test_check_direction_factor_lower_bound()
test_check_direction_factor_upper_bound()

test_calculate_vessel_beam()
test_calculate_vessel_height()
test_calculate_vessel_draft()

test_calculate_end_area()
test_calculate_wind_force()

print("Yippee! Passed all tests")