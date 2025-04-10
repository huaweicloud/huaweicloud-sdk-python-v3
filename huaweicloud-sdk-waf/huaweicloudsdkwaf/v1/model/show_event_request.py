# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEventRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'enterprise_project_id': 'str',
        'eventid': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'enterprise_project_id': 'enterprise_project_id',
        'eventid': 'eventid'
    }

    def __init__(self, x_language=None, enterprise_project_id=None, eventid=None):
        r"""ShowEventRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言，默认值为en-us。zh-cn（中文）/en-us（英文）
        :type x_language: str
        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。
        :type enterprise_project_id: str
        :param eventid: 防护事件id,通过调用查询攻击事件列表(ListEvent)接口获取防护事件id
        :type eventid: str
        """
        
        

        self._x_language = None
        self._enterprise_project_id = None
        self._eventid = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.eventid = eventid

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowEventRequest.

        语言，默认值为en-us。zh-cn（中文）/en-us（英文）

        :return: The x_language of this ShowEventRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowEventRequest.

        语言，默认值为en-us。zh-cn（中文）/en-us（英文）

        :param x_language: The x_language of this ShowEventRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowEventRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。

        :return: The enterprise_project_id of this ShowEventRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowEventRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。

        :param enterprise_project_id: The enterprise_project_id of this ShowEventRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def eventid(self):
        r"""Gets the eventid of this ShowEventRequest.

        防护事件id,通过调用查询攻击事件列表(ListEvent)接口获取防护事件id

        :return: The eventid of this ShowEventRequest.
        :rtype: str
        """
        return self._eventid

    @eventid.setter
    def eventid(self, eventid):
        r"""Sets the eventid of this ShowEventRequest.

        防护事件id,通过调用查询攻击事件列表(ListEvent)接口获取防护事件id

        :param eventid: The eventid of this ShowEventRequest.
        :type eventid: str
        """
        self._eventid = eventid

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
        if not isinstance(other, ShowEventRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
