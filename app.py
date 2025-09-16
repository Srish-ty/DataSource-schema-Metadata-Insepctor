
"""
SourceSense: Intelligent Metadata Extraction Application
Built using Atlan's Apps Framework

This is the main entry point for the SourceSense application.
"""

import streamlit as st
import os
import sys
from pathlib import Path

# Add the src directory to the Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from config.settings import AppSettings
from ui.pages import home, connection, results
from utils.validators import validate_environment

# Initialize app settings
settings = AppSettings()

def main():
    """Main application entry point"""
    
    # Set page configuration
    st.set_page_config(
        page_title="SourceSense - Metadata Intelligence",
        page_icon="🔍",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Validate environment setup
    if not validate_environment():
        st.error("Environment setup incomplete. Please check your configuration.")
        st.stop()
    
    # Initialize session state
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'home'
    if 'connection_status' not in st.session_state:
        st.session_state.connection_status = 'disconnected'
    if 'extracted_metadata' not in st.session_state:
        st.session_state.extracted_metadata = None
    
    # App header
    st.title("🔍 SourceSense")
    st.markdown("**Intelligent Metadata Extraction for Data Sources**")
    st.markdown("---")
    
    # Sidebar navigation
    with st.sidebar:
        st.header("Navigation")
        
        # Navigation buttons
        if st.button("🏠 Home", use_container_width=True):
            st.session_state.current_page = 'home'
        
        if st.button("🔌 Connection", use_container_width=True):
            st.session_state.current_page = 'connection'
        
        if st.button("📊 Results", use_container_width=True):
            st.session_state.current_page = 'results'
        
        # Connection status indicator
        st.markdown("---")
        st.subheader("Status")
        status_color = "🟢" if st.session_state.connection_status == 'connected' else "🔴"
        st.markdown(f"{status_color} **{st.session_state.connection_status.title()}**")
        
        # App info
        st.markdown("---")
        st.markdown("### About SourceSense")
        st.markdown("""
        SourceSense extracts intelligent metadata from various data sources:
        
        **Features:**
        - 📋 Schema Information
        - 💬 Business Context
        - 📈 Quality Metrics
        - 🔄 Lineage Tracking
        
        **Supported Sources:**
        - PostgreSQL
        - MySQL (Coming Soon)
        - MongoDB (Coming Soon)
        """)
    
    # Route to appropriate page
    if st.session_state.current_page == 'home':
        home.render()
    elif st.session_state.current_page == 'connection':
        connection.render()
    elif st.session_state.current_page == 'results':
        results.render()
    else:
        home.render()
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: gray;'>"
        "Built with ❤️ using Atlan's Apps Framework | SourceSense v1.0"
        "</div>", 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()