# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BusinessRiskItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'risk_id': 'str',
        'risk_url': 'str',
        'risk_type': 'str',
        'find_time': 'str',
        'risk_content': 'str',
        'risk_status': 'str'
    }

    attribute_map = {
        'risk_id': 'risk_id',
        'risk_url': 'risk_url',
        'risk_type': 'risk_type',
        'find_time': 'find_time',
        'risk_content': 'risk_content',
        'risk_status': 'risk_status'
    }

    def __init__(self, risk_id=None, risk_url=None, risk_type=None, find_time=None, risk_content=None, risk_status=None):
        """BusinessRiskItem

        The model defined in huaweicloud sdk

        :param risk_id: 业务风险ID
        :type risk_id: str
        :param risk_url: 有风险的URL
        :type risk_url: str
        :param risk_type: 业务风险类型:   * text - 不合规文字   * image - 不合规图片   * dead_link - 不合规链接（死链）   * dark_link - 不合规链接（暗链）   * business_risk - 业务风险 
        :type risk_type: str
        :param find_time: 业务风险发现时间
        :type find_time: str
        :param risk_content: 业务风险内容
        :type risk_content: str
        :param risk_status: 漏洞状态:   * repairing - 未修复   * repaired - 已修复   * false_report - 误报，已忽略 
        :type risk_status: str
        """
        
        

        self._risk_id = None
        self._risk_url = None
        self._risk_type = None
        self._find_time = None
        self._risk_content = None
        self._risk_status = None
        self.discriminator = None

        if risk_id is not None:
            self.risk_id = risk_id
        if risk_url is not None:
            self.risk_url = risk_url
        if risk_type is not None:
            self.risk_type = risk_type
        if find_time is not None:
            self.find_time = find_time
        if risk_content is not None:
            self.risk_content = risk_content
        if risk_status is not None:
            self.risk_status = risk_status

    @property
    def risk_id(self):
        """Gets the risk_id of this BusinessRiskItem.

        业务风险ID

        :return: The risk_id of this BusinessRiskItem.
        :rtype: str
        """
        return self._risk_id

    @risk_id.setter
    def risk_id(self, risk_id):
        """Sets the risk_id of this BusinessRiskItem.

        业务风险ID

        :param risk_id: The risk_id of this BusinessRiskItem.
        :type risk_id: str
        """
        self._risk_id = risk_id

    @property
    def risk_url(self):
        """Gets the risk_url of this BusinessRiskItem.

        有风险的URL

        :return: The risk_url of this BusinessRiskItem.
        :rtype: str
        """
        return self._risk_url

    @risk_url.setter
    def risk_url(self, risk_url):
        """Sets the risk_url of this BusinessRiskItem.

        有风险的URL

        :param risk_url: The risk_url of this BusinessRiskItem.
        :type risk_url: str
        """
        self._risk_url = risk_url

    @property
    def risk_type(self):
        """Gets the risk_type of this BusinessRiskItem.

        业务风险类型:   * text - 不合规文字   * image - 不合规图片   * dead_link - 不合规链接（死链）   * dark_link - 不合规链接（暗链）   * business_risk - 业务风险 

        :return: The risk_type of this BusinessRiskItem.
        :rtype: str
        """
        return self._risk_type

    @risk_type.setter
    def risk_type(self, risk_type):
        """Sets the risk_type of this BusinessRiskItem.

        业务风险类型:   * text - 不合规文字   * image - 不合规图片   * dead_link - 不合规链接（死链）   * dark_link - 不合规链接（暗链）   * business_risk - 业务风险 

        :param risk_type: The risk_type of this BusinessRiskItem.
        :type risk_type: str
        """
        self._risk_type = risk_type

    @property
    def find_time(self):
        """Gets the find_time of this BusinessRiskItem.

        业务风险发现时间

        :return: The find_time of this BusinessRiskItem.
        :rtype: str
        """
        return self._find_time

    @find_time.setter
    def find_time(self, find_time):
        """Sets the find_time of this BusinessRiskItem.

        业务风险发现时间

        :param find_time: The find_time of this BusinessRiskItem.
        :type find_time: str
        """
        self._find_time = find_time

    @property
    def risk_content(self):
        """Gets the risk_content of this BusinessRiskItem.

        业务风险内容

        :return: The risk_content of this BusinessRiskItem.
        :rtype: str
        """
        return self._risk_content

    @risk_content.setter
    def risk_content(self, risk_content):
        """Sets the risk_content of this BusinessRiskItem.

        业务风险内容

        :param risk_content: The risk_content of this BusinessRiskItem.
        :type risk_content: str
        """
        self._risk_content = risk_content

    @property
    def risk_status(self):
        """Gets the risk_status of this BusinessRiskItem.

        漏洞状态:   * repairing - 未修复   * repaired - 已修复   * false_report - 误报，已忽略 

        :return: The risk_status of this BusinessRiskItem.
        :rtype: str
        """
        return self._risk_status

    @risk_status.setter
    def risk_status(self, risk_status):
        """Sets the risk_status of this BusinessRiskItem.

        漏洞状态:   * repairing - 未修复   * repaired - 已修复   * false_report - 误报，已忽略 

        :param risk_status: The risk_status of this BusinessRiskItem.
        :type risk_status: str
        """
        self._risk_status = risk_status

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
        if not isinstance(other, BusinessRiskItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
