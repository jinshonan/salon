<script setup></script>

<template>
    <footer class="bg-blue-800 text-white px-8 py-10">
      <div class="container mx-auto">
        <!-- Salon Information Header -->
        <h2 class="text-4xl mb-1 font-light">Information</h2>
        <p class="text-sm mb-8">店舗情報</p>
        
        <!-- Salon Details -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div>
            <h3 class="text-xl mb-3">Salon (サロン)</h3>
            <p class="mb-1">104-XXXX 東京都XX区XX0-0-0 XXビルXF</p>
            <p class="mb-8">03-XXXX-XXXX</p>
            
            <!-- Business Hours -->
            <h3 class="text-xl mb-4">営業時間</h3>
            <div class="border-b border-blue-600 mb-2">
              <div class="flex justify-between mb-2">
                <span>平日</span>
                <span>11:00 - 21:00</span>
              </div>
            </div>
            <div class="border-b border-blue-600 mb-6">
              <div class="flex justify-between mb-2">
                <span>土/日/祝</span>
                <span>10:00 - 20:00</span>
              </div>
            </div>

            <p class="mb-2">ご予約は24時間受付中のオンライン予約が簡単・便利です。キャンセル、変更も行えます。</p>
            <p>※各種カード、Paypay、QRコード決済でのお支払いが可能です。</p>
          </div>
          
          <!-- Right column - can be used for map or additional info -->
          <div class="flex items-center justify-center">
            <!-- This space can be used for a map or other content -->
          </div>
        </div>
        
        <!-- Social Media Link -->
        <div class="flex justify-center mt-8 mb-6">
          <a href="https://instagram.com/" class="flex items-center text-white hover:text-blue-300 transition">
            <svg class="w-5 h-5 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
              <path fill="currentColor" d="M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9S339 319.5 339 255.9 287.7 141 224.1 141zm0 189.6c-41.1 0-74.7-33.5-74.7-74.7s33.5-74.7 74.7-74.7 74.7 33.5 74.7 74.7-33.6 74.7-74.7 74.7zm146.4-194.3c0 14.9-12 26.8-26.8 26.8-14.9 0-26.8-12-26.8-26.8s12-26.8 26.8-26.8 26.8 12 26.8 26.8zm76.1 27.2c-1.7-35.9-9.9-67.7-36.2-93.9-26.2-26.2-58-34.4-93.9-36.2-37-2.1-147.9-2.1-184.9 0-35.8 1.7-67.6 9.9-93.9 36.1s-34.4 58-36.2 93.9c-2.1 37-2.1 147.9 0 184.9 1.7 35.9 9.9 67.7 36.2 93.9s58 34.4 93.9 36.2c37 2.1 147.9 2.1 184.9 0 35.9-1.7 67.7-9.9 93.9-36.2 26.2-26.2 34.4-58 36.2-93.9 2.1-37 2.1-147.8 0-184.8zM398.8 388c-7.8 19.6-22.9 34.7-42.6 42.6-29.5 11.7-99.5 9-132.1 9s-102.7 2.6-132.1-9c-19.6-7.8-34.7-22.9-42.6-42.6-11.7-29.5-9-99.5-9-132.1s-2.6-102.7 9-132.1c7.8-19.6 22.9-34.7 42.6-42.6 29.5-11.7 99.5-9 132.1-9s102.7-2.6 132.1 9c19.6 7.8 34.7 22.9 42.6 42.6 11.7 29.5 9 99.5 9 132.1s2.7 102.7-9 132.1z"></path>
            </svg>
            Salon Instagram
          </a>
        </div>
        
        <!-- Copyright -->
        <div class="text-center text-sm">
          Copyright 2016 Salon. All rights reserved.
        </div>
      </div>
    </footer>
  </template>
