# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DocumentCreateRequestData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'format': 'str',
        'frame_interval': 'int'
    }

    attribute_map = {
        'url': 'url',
        'format': 'format',
        'frame_interval': 'frame_interval'
    }

    def __init__(self, url=None, format=None, frame_interval=None):
        """DocumentCreateRequestData

        The model defined in huaweicloud sdk

        :param url: 文档url
        :type url: str
        :param format: 文档格式。可选值： docx pdf doc xls xlsx ppt pptx pps ppsx xltx xltm xlsb xlsm txt csv epub webpage 若format与文档实际格式不一致，则返回报错参数错误
        :type format: str
        :param frame_interval: 当需要审核网页视频时，视频截帧频率间隔，单位为秒，取值范围为1~60s；若不传递默认5s截帧一次
        :type frame_interval: int
        """
        
        

        self._url = None
        self._format = None
        self._frame_interval = None
        self.discriminator = None

        self.url = url
        self.format = format
        if frame_interval is not None:
            self.frame_interval = frame_interval

    @property
    def url(self):
        """Gets the url of this DocumentCreateRequestData.

        文档url

        :return: The url of this DocumentCreateRequestData.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DocumentCreateRequestData.

        文档url

        :param url: The url of this DocumentCreateRequestData.
        :type url: str
        """
        self._url = url

    @property
    def format(self):
        """Gets the format of this DocumentCreateRequestData.

        文档格式。可选值： docx pdf doc xls xlsx ppt pptx pps ppsx xltx xltm xlsb xlsm txt csv epub webpage 若format与文档实际格式不一致，则返回报错参数错误

        :return: The format of this DocumentCreateRequestData.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this DocumentCreateRequestData.

        文档格式。可选值： docx pdf doc xls xlsx ppt pptx pps ppsx xltx xltm xlsb xlsm txt csv epub webpage 若format与文档实际格式不一致，则返回报错参数错误

        :param format: The format of this DocumentCreateRequestData.
        :type format: str
        """
        self._format = format

    @property
    def frame_interval(self):
        """Gets the frame_interval of this DocumentCreateRequestData.

        当需要审核网页视频时，视频截帧频率间隔，单位为秒，取值范围为1~60s；若不传递默认5s截帧一次

        :return: The frame_interval of this DocumentCreateRequestData.
        :rtype: int
        """
        return self._frame_interval

    @frame_interval.setter
    def frame_interval(self, frame_interval):
        """Sets the frame_interval of this DocumentCreateRequestData.

        当需要审核网页视频时，视频截帧频率间隔，单位为秒，取值范围为1~60s；若不传递默认5s截帧一次

        :param frame_interval: The frame_interval of this DocumentCreateRequestData.
        :type frame_interval: int
        """
        self._frame_interval = frame_interval

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DocumentCreateRequestData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
