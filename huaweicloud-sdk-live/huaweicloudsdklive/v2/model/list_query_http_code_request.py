# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListQueryHttpCodeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'play_domains': 'list[str]',
        'code': 'list[str]',
        'region': 'list[str]',
        'isp': 'list[str]',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'play_domains': 'play_domains',
        'code': 'code',
        'region': 'region',
        'isp': 'isp',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, play_domains=None, code=None, region=None, isp=None, start_time=None, end_time=None):
        """ListQueryHttpCodeRequest

        The model defined in huaweicloud sdk

        :param play_domains: 播放域名列表，最多支持查询100个域名，多个域名以逗号分隔。 
        :type play_domains: list[str]
        :param code: 状态码。 
        :type code: list[str]
        :param region: 区域列表。具体取值请参考[省份名称缩写](live_03_0043.xml)，不填写查询所有区域。 
        :type region: list[str]
        :param isp: 运营商列表，取值如下： - CMCC ：移动 - CTCC ： 电信 - CUCC ：联通 - OTHER ：其他  不填写查询所有运营商。 
        :type isp: list[str]
        :param start_time: 起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。若参数为空，默认查询最近1小时数据。  最大查询跨度1天，最大查询周期7天。 
        :type start_time: str
        :param end_time: 结束时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。  若参数为空，默认为当前时间。结束时间需大于起始时间。  最大查询跨度1天，最大查询周期7天。 
        :type end_time: str
        """
        
        

        self._play_domains = None
        self._code = None
        self._region = None
        self._isp = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.play_domains = play_domains
        if code is not None:
            self.code = code
        if region is not None:
            self.region = region
        if isp is not None:
            self.isp = isp
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def play_domains(self):
        """Gets the play_domains of this ListQueryHttpCodeRequest.

        播放域名列表，最多支持查询100个域名，多个域名以逗号分隔。 

        :return: The play_domains of this ListQueryHttpCodeRequest.
        :rtype: list[str]
        """
        return self._play_domains

    @play_domains.setter
    def play_domains(self, play_domains):
        """Sets the play_domains of this ListQueryHttpCodeRequest.

        播放域名列表，最多支持查询100个域名，多个域名以逗号分隔。 

        :param play_domains: The play_domains of this ListQueryHttpCodeRequest.
        :type play_domains: list[str]
        """
        self._play_domains = play_domains

    @property
    def code(self):
        """Gets the code of this ListQueryHttpCodeRequest.

        状态码。 

        :return: The code of this ListQueryHttpCodeRequest.
        :rtype: list[str]
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ListQueryHttpCodeRequest.

        状态码。 

        :param code: The code of this ListQueryHttpCodeRequest.
        :type code: list[str]
        """
        self._code = code

    @property
    def region(self):
        """Gets the region of this ListQueryHttpCodeRequest.

        区域列表。具体取值请参考[省份名称缩写](live_03_0043.xml)，不填写查询所有区域。 

        :return: The region of this ListQueryHttpCodeRequest.
        :rtype: list[str]
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListQueryHttpCodeRequest.

        区域列表。具体取值请参考[省份名称缩写](live_03_0043.xml)，不填写查询所有区域。 

        :param region: The region of this ListQueryHttpCodeRequest.
        :type region: list[str]
        """
        self._region = region

    @property
    def isp(self):
        """Gets the isp of this ListQueryHttpCodeRequest.

        运营商列表，取值如下： - CMCC ：移动 - CTCC ： 电信 - CUCC ：联通 - OTHER ：其他  不填写查询所有运营商。 

        :return: The isp of this ListQueryHttpCodeRequest.
        :rtype: list[str]
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this ListQueryHttpCodeRequest.

        运营商列表，取值如下： - CMCC ：移动 - CTCC ： 电信 - CUCC ：联通 - OTHER ：其他  不填写查询所有运营商。 

        :param isp: The isp of this ListQueryHttpCodeRequest.
        :type isp: list[str]
        """
        self._isp = isp

    @property
    def start_time(self):
        """Gets the start_time of this ListQueryHttpCodeRequest.

        起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。若参数为空，默认查询最近1小时数据。  最大查询跨度1天，最大查询周期7天。 

        :return: The start_time of this ListQueryHttpCodeRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListQueryHttpCodeRequest.

        起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。若参数为空，默认查询最近1小时数据。  最大查询跨度1天，最大查询周期7天。 

        :param start_time: The start_time of this ListQueryHttpCodeRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListQueryHttpCodeRequest.

        结束时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。  若参数为空，默认为当前时间。结束时间需大于起始时间。  最大查询跨度1天，最大查询周期7天。 

        :return: The end_time of this ListQueryHttpCodeRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListQueryHttpCodeRequest.

        结束时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。  若参数为空，默认为当前时间。结束时间需大于起始时间。  最大查询跨度1天，最大查询周期7天。 

        :param end_time: The end_time of this ListQueryHttpCodeRequest.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ListQueryHttpCodeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
