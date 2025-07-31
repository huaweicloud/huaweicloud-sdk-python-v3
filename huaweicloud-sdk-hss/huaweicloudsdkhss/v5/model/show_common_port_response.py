# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCommonPortResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port': 'int',
        'type': 'str',
        'status': 'str',
        'description': 'str',
        'description_en': 'str'
    }

    attribute_map = {
        'port': 'port',
        'type': 'type',
        'status': 'status',
        'description': 'description',
        'description_en': 'description_en'
    }

    def __init__(self, port=None, type=None, status=None, description=None, description_en=None):
        r"""ShowCommonPortResponse

        The model defined in huaweicloud sdk

        :param port: 端口号
        :type port: int
        :param type: 端口类型：目前包括TCP，UDP两种
        :type type: str
        :param status: 状态   - normal : 正常   - danger : 危险   - unknow : 未知
        :type status: str
        :param description: 中文描述
        :type description: str
        :param description_en: 英文描述
        :type description_en: str
        """
        
        super(ShowCommonPortResponse, self).__init__()

        self._port = None
        self._type = None
        self._status = None
        self._description = None
        self._description_en = None
        self.discriminator = None

        if port is not None:
            self.port = port
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description
        if description_en is not None:
            self.description_en = description_en

    @property
    def port(self):
        r"""Gets the port of this ShowCommonPortResponse.

        端口号

        :return: The port of this ShowCommonPortResponse.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this ShowCommonPortResponse.

        端口号

        :param port: The port of this ShowCommonPortResponse.
        :type port: int
        """
        self._port = port

    @property
    def type(self):
        r"""Gets the type of this ShowCommonPortResponse.

        端口类型：目前包括TCP，UDP两种

        :return: The type of this ShowCommonPortResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowCommonPortResponse.

        端口类型：目前包括TCP，UDP两种

        :param type: The type of this ShowCommonPortResponse.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this ShowCommonPortResponse.

        状态   - normal : 正常   - danger : 危险   - unknow : 未知

        :return: The status of this ShowCommonPortResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowCommonPortResponse.

        状态   - normal : 正常   - danger : 危险   - unknow : 未知

        :param status: The status of this ShowCommonPortResponse.
        :type status: str
        """
        self._status = status

    @property
    def description(self):
        r"""Gets the description of this ShowCommonPortResponse.

        中文描述

        :return: The description of this ShowCommonPortResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowCommonPortResponse.

        中文描述

        :param description: The description of this ShowCommonPortResponse.
        :type description: str
        """
        self._description = description

    @property
    def description_en(self):
        r"""Gets the description_en of this ShowCommonPortResponse.

        英文描述

        :return: The description_en of this ShowCommonPortResponse.
        :rtype: str
        """
        return self._description_en

    @description_en.setter
    def description_en(self, description_en):
        r"""Sets the description_en of this ShowCommonPortResponse.

        英文描述

        :param description_en: The description_en of this ShowCommonPortResponse.
        :type description_en: str
        """
        self._description_en = description_en

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
        if not isinstance(other, ShowCommonPortResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
