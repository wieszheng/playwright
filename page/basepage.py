# -*- coding:utf-8 -*-

"""
@Version  : Python3.8
@FileName : basepage.py
@Time     : 2023/8/26 15:56
@Author   : ShiWeiZheng
@Function :
"""
import asyncio

from playwright.async_api import async_playwright
from playwright.sync_api import Page


class Basepage:

    def __init__(self, page: Page):
        """
        初始化page
        :param page:context.new_page
        """
        self.page = page

    def _goto_url(self, url):
        """打开网址"""
        self.page.goto(url)

    def _click(self, locator, frame_locator=None):
        """
        点击元素
        :param locator: 传入元素定位器
        :param frame_locator: 传入frame框架的的定位器，如果没有传入，则一般点击
        :return:
        """
        try:
            if frame_locator is not None:
                self.page.frame_locator(frame_locator).locator(locator).click()
            else:
                self.page.click(locator)
        except Exception as e:
            print(e)


class AsyncBasePage:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    async def initialize(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=False)
        self.context = await self.browser.new_context()
        self.page = await self.context.new_page()

    async def close(self):
        await self.page.close()
        await self.context.close()
        await self.browser.close()

    async def goto(self, url):
        await self.page.goto(url)

    async def click(self, selector):
        await self.page.click(selector)

    async def type(self, selector, text):
        await self.page.type(selector, text)

    async def screenshot(self, path):
        await self.page.screenshot(path)


if __name__ == '__main__':
    async def main():
        screenshot_helper = AsyncBasePage()
        await screenshot_helper.initialize()
        await screenshot_helper.goto('https://www.baidu.com/')
        await screenshot_helper.close()


    asyncio.get_event_loop().run_until_complete(main())