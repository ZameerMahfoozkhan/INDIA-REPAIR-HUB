import os
import re

dir_path = r"c:\Users\zamee\Desktop\indiarepairhub"

replacements = [
    (r"SERVICE CENTER INDIA", "INDIA REPAIR HUB"),
    (r"Service Center India", "India Repair Hub"),
    (r"Service Center India's", "India Repair Hub's"),
    (r"LED, LCD, and Smart TVs", "ACs, Fridges, Washing Machines, Microwaves, and TVs"),
    (r"LED, LCD & Smart TV", "AC, Fridge, Washing Machine, Microwave & TV"),
    (r"TV Repair Service", "Home Appliance Repair Service"),
    (r"TV repair service", "home appliance repair service"),
    (r"TV repair in", "home appliance repair in"),
    (r"TV Repair", "Home Appliance Repair"),
    (r"TV repair", "home appliance repair"),
    (r"TV issue", "appliance issue"),
    (r"TV issues", "appliance issues"),
    (r"TV service centre", "appliance service centre"),
    (r"TV Service Centre", "Appliance Service Centre"),
    (r"your TV", "your appliance"),
    (r"any TV brand", "any appliance brand"),
    (r"Complete Home Appliance Repair Solutions", "Complete Home Appliance Repair Solutions"), # Just in case it was already replaced
    (r"Complete TV Repair Solutions", "Complete Home Appliance Repair Solutions"),
    (r"(?<!91)9120992012", "+919120992012"), # replace 9120992012 with +919120992012, unless preceded by 91 (for whatsapp link)
]

new_services_grid = """    <div class="services-grid">
      <a href="tel:+919120992012" class="service-card" id="serviceAc">
        <div class="s-icon">❄️</div>
        <h3>AC Repair</h3>
        <p>Expert cooling solutions, gas refilling, servicing, and compressor repair for all AC brands.</p>
      </a>
      <a href="tel:+919120992012" class="service-card" id="serviceFridge">
        <div class="s-icon">🧊</div>
        <h3>Refrigerator Repair</h3>
        <p>Professional troubleshooting for cooling issues, compressor changes, and thermostat repairs.</p>
      </a>
      <a href="tel:+919120992012" class="service-card" id="serviceWashingMachine">
        <div class="s-icon">🧺</div>
        <h3>Washing Machine Repair</h3>
        <p>Drum repairs, motor replacement, water leakage fixes for front-load and top-load machines.</p>
      </a>
      <a href="tel:+919120992012" class="service-card" id="serviceMicrowave">
        <div class="s-icon">♨️</div>
        <h3>Microwave Repair</h3>
        <p>Heating issue fixes, magnetron replacement, and touch panel repair for all microwaves.</p>
      </a>
      <a href="tel:+919120992012" class="service-card" id="serviceTv">
        <div class="s-icon">📺</div>
        <h3>TV Repair</h3>
        <p>Expert repair for LED, LCD, and Smart TVs including screen and motherboard issues.</p>
      </a>
      <a href="tel:+919120992012" class="service-card" id="serviceGeyser">
        <div class="s-icon">🚿</div>
        <h3>Geyser Repair</h3>
        <p>Heating element replacements, thermostat fixes, and leak repairs for water heaters.</p>
      </a>
      <a href="tel:+919120992012" class="service-card" id="serviceRO">
        <div class="s-icon">💧</div>
        <h3>RO / Water Purifier</h3>
        <p>Filter changes, pump repairs, and comprehensive servicing for clean, safe water.</p>
      </a>
      <a href="tel:+919120992012" class="service-card" id="serviceChimney">
        <div class="s-icon">💨</div>
        <h3>Chimney Repair</h3>
        <p>Motor repairs, deep cleaning, and button panel fixes for kitchen chimneys.</p>
      </div>"""

for filename in os.listdir(dir_path):
    if filename.endswith(".html"):
        file_path = os.path.join(dir_path, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace text replacements
        for old, new in replacements:
            content = re.sub(old, new, content)
            
        # specifically replace services grid in index.html
        if filename == "index.html":
            # We match the entire <div class="services-grid"> ... </div>
            # Since regex with re.DOTALL can be tricky, we'll try to find it
            pattern = re.compile(r'<div class="services-grid">.*?(?=\s*</div>\s*</section>)</div>', re.DOTALL)
            content = pattern.sub(new_services_grid, content)
            
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

print("Replacement complete.")
