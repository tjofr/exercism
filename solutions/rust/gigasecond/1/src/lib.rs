use time::PrimitiveDateTime as DateTime;
use time::ext::NumericalDuration;

// Returns a DateTime one billion seconds after start.
pub fn after(start: DateTime) -> DateTime {
    //todo!("What time is a gigasecond later than {start}");
    start+1_000_000_000_i64.seconds()
}
