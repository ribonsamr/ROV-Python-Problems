from quiz2 import quiz2


def main():
  test_cases = [
      ('1804', True), ('1805', False), ('1806', False), ('1807', False),
      ('1808', True), ('1809', False), ('1810', False), ('1811', False),
      ('1812', True), ('1813', False), ('1814', False), ('1815', False),
      ('1816', True), ('1817', False), ('1818', False), ('1819', False),
      ('1820', True), ('1821', False), ('1822', False), ('1823', False),
      ('1824', True), ('1825', False), ('1826', False), ('1827', False),
      ('1828', True), ('1829', False), ('1830', False), ('1831', False),
      ('1832', True), ('1833', False), ('1834', False), ('1835', False),
      ('1836', True), ('1837', False), ('1838', False), ('1839', False),
      ('1840', True), ('1841', False), ('1842', False), ('1843', False),
      ('1844', True), ('1845', False), ('1846', False), ('1847', False),
      ('1848', True), ('1849', False), ('1850', False), ('1851', False),
      ('1852', True), ('1853', False), ('1854', False), ('1855', False),
      ('1856', True), ('1857', False), ('1858', False), ('1859', False),
      ('1860', True), ('1861', False), ('1862', False), ('1863', False),
      ('1864', True), ('1865', False), ('1866', False), ('1867', False),
      ('1868', True), ('1869', False), ('1870', False), ('1871', False),
      ('1872', True), ('1873', False), ('1874', False), ('1875', False),
      ('1876', True), ('1877', False), ('1878', False), ('1879', False),
      ('1880', True), ('1881', False), ('1882', False), ('1883', False),
      ('1884', True), ('1885', False), ('1886', False), ('1887', False),
      ('1888', True), ('1889', False), ('1890', False), ('1891', False),
      ('1892', True), ('1893', False), ('1894', False), ('1895', False),
      ('1896', True), ('1897', False), ('1898', False), ('1899', False),
      ('1900', False), ('1901', False), ('1902', False), ('1903', False),
      ('1904', True), ('1905', False), ('1906', False), ('1907', False),
      ('1908', True), ('1909', False), ('1910', False), ('1911', False),
      ('1912', True), ('1913', False), ('1914', False), ('1915', False),
      ('1916', True), ('1917', False), ('1918', False), ('1919', False),
      ('1920', True), ('1921', False), ('1922', False), ('1923', False),
      ('1924', True), ('1925', False), ('1926', False), ('1927', False),
      ('1928', True), ('1929', False), ('1930', False), ('1931', False),
      ('1932', True), ('1933', False), ('1934', False), ('1935', False),
      ('1936', True), ('1937', False), ('1938', False), ('1939', False),
      ('1940', True), ('1941', False), ('1942', False), ('1943', False),
      ('1944', True), ('1945', False), ('1946', False), ('1947', False),
      ('1948', True), ('1949', False), ('1950', False), ('1951', False),
      ('1952', True), ('1953', False), ('1954', False), ('1955', False),
      ('1956', True), ('1957', False), ('1958', False), ('1959', False),
      ('1960', True), ('1961', False), ('1962', False), ('1963', False),
      ('1964', True), ('1965', False), ('1966', False), ('1967', False),
      ('1968', True), ('1969', False), ('1970', False), ('1971', False),
      ('1972', True), ('1973', False), ('1974', False), ('1975', False),
      ('1976', True), ('1977', False), ('1978', False), ('1979', False),
      ('1980', True), ('1981', False), ('1982', False), ('1983', False),
      ('1984', True), ('1985', False), ('1986', False), ('1987', False),
      ('1988', True), ('1989', False), ('1990', False), ('1991', False),
      ('1992', True), ('1993', False), ('1994', False), ('1995', False),
      ('1996', True), ('1997', False), ('1998', False), ('1999', False),
      ('2000', True), ('2001', False), ('2002', False), ('2003', False),
      ('2004', True), ('2005', False), ('2006', False), ('2007', False),
      ('2008', True), ('2009', False), ('2010', False), ('2011', False),
      ('2012', True), ('2013', False), ('2014', False), ('2015', False),
      ('2016', True), ('2017', False), ('2018', False), ('2019', False),
      ('2020', True), ('2021', False), ('2022', False), ('2023', False),
      ('2024', True), ('2025', False), ('2026', False), ('2027', False),
      ('2028', True), ('2029', False), ('2030', False), ('2031', False),
      ('2032', True), ('2033', False), ('2034', False), ('2035', False),
      ('2036', True), ('2037', False), ('2038', False), ('2039', False),
      ('2040', True), ('2041', False), ('2042', False), ('2043', False),
      ('2044', True), ('2045', False), ('2046', False), ('2047', False),
      ('2048', True), ('2049', False), ('2050', False), ('2051', False),
      ('2052', True), ('2053', False), ('2054', False), ('2055', False),
      ('2056', True), ('2057', False), ('2058', False), ('2059', False),
      ('2060', True), ('2061', False), ('2062', False), ('2063', False),
      ('2064', True), ('2065', False), ('2066', False), ('2067', False),
      ('2068', True), ('2069', False), ('2070', False), ('2071', False),
      ('2072', True), ('2073', False), ('2074', False), ('2075', False),
      ('2076', True), ('2077', False), ('2078', False), ('2079', False),
      ('2080', True), ('2081', False), ('2082', False), ('2083', False),
      ('2084', True), ('2085', False), ('2086', False), ('2087', False),
      ('2088', True), ('2089', False), ('2090', False), ('2091', False),
      ('2092', True), ('2093', False), ('2094', False), ('2095', False),
      ('2096', True), ('2097', False), ('2098', False), ('2099', False),
      ('2100', False), ('2101', False), ('2102', False), ('2103', False),
      ('2104', True), ('2105', False), ('2106', False), ('2107', False),
      ('2108', True), ('2109', False), ('2110', False), ('2111', False),
      ('2112', True), ('2113', False), ('2114', False), ('2115', False),
      ('2116', True), ('2117', False), ('2118', False), ('2119', False),
      ('2120', True), ('2121', False), ('2122', False), ('2123', False),
      ('2124', True), ('2125', False), ('2126', False), ('2127', False),
      ('2128', True), ('2129', False), ('2130', False), ('2131', False),
      ('2132', True), ('2133', False), ('2134', False), ('2135', False),
      ('2136', True), ('2137', False), ('2138', False), ('2139', False),
      ('2140', True), ('2141', False), ('2142', False), ('2143', False),
      ('2144', True), ('2145', False), ('2146', False), ('2147', False),
      ('2148', True), ('2149', False), ('2150', False), ('2151', False),
      ('2152', True), ('2153', False), ('2154', False), ('2155', False),
      ('2156', True), ('2157', False), ('2158', False), ('2159', False),
      ('2160', True), ('2161', False), ('2162', False), ('2163', False),
      ('2164', True), ('2165', False), ('2166', False), ('2167', False),
      ('2168', True), ('2169', False), ('2170', False), ('2171', False),
      ('2172', True), ('2173', False), ('2174', False), ('2175', False),
      ('2176', True), ('2177', False), ('2178', False), ('2179', False),
      ('2180', True), ('2181', False), ('2182', False), ('2183', False),
      ('2184', True), ('2185', False), ('2186', False), ('2187', False),
      ('2188', True), ('2189', False), ('2190', False), ('2191', False),
      ('2192', True), ('2193', False), ('2194', False), ('2195', False),
      ('2196', True), ('2197', False), ('2198', False), ('2199', False),
      ('2200', False), ('2201', False), ('2202', False), ('2203', False),
      ('2204', True), ('2205', False), ('2206', False), ('2207', False),
      ('2208', True), ('2209', False), ('2210', False), ('2211', False),
      ('2212', True), ('2213', False), ('2214', False), ('2215', False),
      ('2216', True), ('2217', False), ('2218', False), ('2219', False),
      ('2220', True), ('2221', False), ('2222', False), ('2223', False),
      ('2224', True), ('2225', False), ('2226', False), ('2227', False),
      ('2228', True), ('2229', False), ('2230', False), ('2231', False),
      ('2232', True), ('2233', False), ('2234', False), ('2235', False),
      ('2236', True), ('2237', False), ('2238', False), ('2239', False),
      ('2240', True), ('2241', False), ('2242', False), ('2243', False),
      ('2244', True), ('2245', False), ('2246', False), ('2247', False),
      ('2248', True), ('2249', False), ('2250', False), ('2251', False),
      ('2252', True), ('2253', False), ('2254', False), ('2255', False),
      ('2256', True), ('2257', False), ('2258', False), ('2259', False),
      ('2260', True), ('2261', False), ('2262', False), ('2263', False),
      ('2264', True), ('2265', False), ('2266', False), ('2267', False),
      ('2268', True), ('2269', False), ('2270', False), ('2271', False),
      ('2272', True), ('2273', False), ('2274', False), ('2275', False),
      ('2276', True), ('2277', False), ('2278', False), ('2279', False),
      ('2280', True), ('2281', False), ('2282', False), ('2283', False),
      ('2284', True), ('2285', False), ('2286', False), ('2287', False),
      ('2288', True), ('2289', False), ('2290', False), ('2291', False),
      ('2292', True), ('2293', False), ('2294', False), ('2295', False),
      ('2296', True), ('2297', False), ('2298', False), ('2299', False),
      ('2300', False), ('2301', False), ('2302', False), ('2303', False),
      ('2304', True), ('2305', False), ('2306', False), ('2307', False),
      ('2308', True), ('2309', False), ('2310', False), ('2311', False),
      ('2312', True), ('2313', False), ('2314', False), ('2315', False),
      ('2316', True), ('2317', False), ('2318', False), ('2319', False),
      ('2320', True), ('2321', False), ('2322', False), ('2323', False),
      ('2324', True), ('2325', False), ('2326', False), ('2327', False),
      ('2328', True), ('2329', False), ('2330', False), ('2331', False),
      ('2332', True), ('2333', False), ('2334', False), ('2335', False),
      ('2336', True), ('2337', False), ('2338', False), ('2339', False),
      ('2340', True), ('2341', False), ('2342', False), ('2343', False),
      ('2344', True), ('2345', False), ('2346', False), ('2347', False),
      ('2348', True), ('2349', False), ('2350', False), ('2351', False),
      ('2352', True), ('2353', False), ('2354', False), ('2355', False),
      ('2356', True), ('2357', False), ('2358', False), ('2359', False),
      ('2360', True), ('2361', False), ('2362', False), ('2363', False),
      ('2364', True), ('2365', False), ('2366', False), ('2367', False),
      ('2368', True), ('2369', False), ('2370', False), ('2371', False),
      ('2372', True), ('2373', False), ('2374', False), ('2375', False),
      ('2376', True), ('2377', False), ('2378', False), ('2379', False),
      ('2380', True), ('2381', False), ('2382', False), ('2383', False),
      ('2384', True), ('2385', False), ('2386', False), ('2387', False),
      ('2388', True), ('2389', False), ('2390', False), ('2391', False),
      ('2392', True), ('2393', False), ('2394', False), ('2395', False),
      ('2396', True), ('2397', False), ('2398', False), ('2399', False),
      ('2400', True)
  ]

  for (number, expected) in test_cases:
    result = quiz2(number)

    if not result == expected:
      print(f"Test failed.".upper())
      print(f"Input: {number}\nExpected: {expected}\nFound: {result}")
      return

  print("TESTS PASSED.")


if __name__ == "__main__":
  main()
