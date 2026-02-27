#!/usr/bin/env python3
"""
Test PDF download functionality
"""

import requests
import pandas as pd
import io

def test_pdf_download():
    """Test the PDF download endpoint"""
    print("🧪 Testing PDF Download Functionality")
    print("=" * 50)
    
    # Create sample CSV data
    data = {
        'cycle': [1, 1, 1, 2, 2, 2, 3, 3, 3],
        'Capacity': [1.5, 1.5, 1.5, 1.45, 1.45, 1.45, 1.4, 1.4, 1.4],
        'Voltage_measured': [4.2, 3.8, 3.5, 4.2, 3.7, 3.4, 4.1, 3.6, 3.3],
        'Current_measured': [-2.0, -2.1, -2.0, -2.0, -2.1, -2.0, -2.0, -2.1, -2.0],
        'Temperature_measured': [25.0, 25.5, 26.0, 24.8, 25.2, 25.8, 24.5, 25.0, 25.5],
        'Time': [0, 1000, 2000, 0, 1000, 2000, 0, 1000, 2000]
    }
    
    df = pd.DataFrame(data)
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_data = csv_buffer.getvalue()
    
    try:
        # Test PDF download endpoint
        print("\n1. Testing PDF download endpoint...")
        files = {'file': ('test_battery.csv', csv_data, 'text/csv')}
        
        response = requests.post('http://localhost:8000/download-report', files=files)
        
        if response.status_code == 200:
            print("✅ PDF download endpoint working")
            
            # Check if response contains PDF data
            content_type = response.headers.get('content-type', '')
            if 'pdf' in content_type:
                print("✅ Response contains PDF content")
                print(f"   Content-Type: {content_type}")
                print(f"   Content-Length: {len(response.content)} bytes")
                
                # Save test PDF
                with open('test_downloaded_report.pdf', 'wb') as f:
                    f.write(response.content)
                print("✅ Test PDF saved as 'test_downloaded_report.pdf'")
                
                return True
            else:
                print(f"❌ Response does not contain PDF content: {content_type}")
                return False
        else:
            print(f"❌ PDF download failed: {response.status_code}")
            print(f"   Error: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to backend. Is it running on port 8000?")
        return False
    except Exception as e:
        print(f"❌ PDF download test failed: {e}")
        return False

if __name__ == "__main__":
    success = test_pdf_download()
    
    print("\n" + "=" * 50)
    if success:
        print("🎉 PDF download test PASSED!")
        print("\n📋 The PDF download feature is working correctly.")
        print("   Users can now download professional battery analysis reports.")
    else:
        print("❌ PDF download test FAILED!")
        print("\n🔧 Troubleshooting:")
        print("   1. Ensure the backend is running on port 8000")
        print("   2. Check that reportlab is installed")
        print("   3. Verify the reports directory exists")
        print("   4. Check backend logs for any errors")
