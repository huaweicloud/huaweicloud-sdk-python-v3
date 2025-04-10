# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScriptsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'int',
        'name_like': 'str',
        'creator': 'str',
        'risk_level': 'str',
        'type': 'str',
        'enterprise_project_id': 'str',
        'x_language': 'str',
        'x_project_id': 'str',
        'x_user_profile': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'name_like': 'name_like',
        'creator': 'creator',
        'risk_level': 'risk_level',
        'type': 'type',
        'enterprise_project_id': 'enterprise_project_id',
        'x_language': 'X-Language',
        'x_project_id': 'x-project-id',
        'x_user_profile': 'x-user-profile'
    }

    def __init__(self, limit=None, marker=None, name_like=None, creator=None, risk_level=None, type=None, enterprise_project_id=None, x_language=None, x_project_id=None, x_user_profile=None):
        r"""ListScriptsRequest

        The model defined in huaweicloud sdk

        :param limit: 分页参数：每页返回记录个数限制
        :type limit: int
        :param marker: 分页参数：上一页最后一个记录id
        :type marker: int
        :param name_like: 脚本名（模糊）
        :type name_like: str
        :param creator: 创建人
        :type creator: str
        :param risk_level: 风险等级 LOW:低风险 MEDIUM：中风险 HIGH：高风险
        :type risk_level: str
        :param type: 脚本类型 SHELL:shell脚本 PYTHON：python脚本 BAT：Bat脚本
        :type type: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param x_language: 国际化标记，zh-cn表示中文，en-us或不传表示英文
        :type x_language: str
        :param x_project_id: 项目ID，一个项目对应一个region
        :type x_project_id: str
        :param x_user_profile: IAM5.0用户信息
        :type x_user_profile: str
        """
        
        

        self._limit = None
        self._marker = None
        self._name_like = None
        self._creator = None
        self._risk_level = None
        self._type = None
        self._enterprise_project_id = None
        self._x_language = None
        self._x_project_id = None
        self._x_user_profile = None
        self.discriminator = None

        self.limit = limit
        if marker is not None:
            self.marker = marker
        if name_like is not None:
            self.name_like = name_like
        if creator is not None:
            self.creator = creator
        if risk_level is not None:
            self.risk_level = risk_level
        if type is not None:
            self.type = type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if x_language is not None:
            self.x_language = x_language
        if x_project_id is not None:
            self.x_project_id = x_project_id
        if x_user_profile is not None:
            self.x_user_profile = x_user_profile

    @property
    def limit(self):
        r"""Gets the limit of this ListScriptsRequest.

        分页参数：每页返回记录个数限制

        :return: The limit of this ListScriptsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListScriptsRequest.

        分页参数：每页返回记录个数限制

        :param limit: The limit of this ListScriptsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListScriptsRequest.

        分页参数：上一页最后一个记录id

        :return: The marker of this ListScriptsRequest.
        :rtype: int
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListScriptsRequest.

        分页参数：上一页最后一个记录id

        :param marker: The marker of this ListScriptsRequest.
        :type marker: int
        """
        self._marker = marker

    @property
    def name_like(self):
        r"""Gets the name_like of this ListScriptsRequest.

        脚本名（模糊）

        :return: The name_like of this ListScriptsRequest.
        :rtype: str
        """
        return self._name_like

    @name_like.setter
    def name_like(self, name_like):
        r"""Sets the name_like of this ListScriptsRequest.

        脚本名（模糊）

        :param name_like: The name_like of this ListScriptsRequest.
        :type name_like: str
        """
        self._name_like = name_like

    @property
    def creator(self):
        r"""Gets the creator of this ListScriptsRequest.

        创建人

        :return: The creator of this ListScriptsRequest.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ListScriptsRequest.

        创建人

        :param creator: The creator of this ListScriptsRequest.
        :type creator: str
        """
        self._creator = creator

    @property
    def risk_level(self):
        r"""Gets the risk_level of this ListScriptsRequest.

        风险等级 LOW:低风险 MEDIUM：中风险 HIGH：高风险

        :return: The risk_level of this ListScriptsRequest.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this ListScriptsRequest.

        风险等级 LOW:低风险 MEDIUM：中风险 HIGH：高风险

        :param risk_level: The risk_level of this ListScriptsRequest.
        :type risk_level: str
        """
        self._risk_level = risk_level

    @property
    def type(self):
        r"""Gets the type of this ListScriptsRequest.

        脚本类型 SHELL:shell脚本 PYTHON：python脚本 BAT：Bat脚本

        :return: The type of this ListScriptsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListScriptsRequest.

        脚本类型 SHELL:shell脚本 PYTHON：python脚本 BAT：Bat脚本

        :param type: The type of this ListScriptsRequest.
        :type type: str
        """
        self._type = type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListScriptsRequest.

        企业项目id

        :return: The enterprise_project_id of this ListScriptsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListScriptsRequest.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ListScriptsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ListScriptsRequest.

        国际化标记，zh-cn表示中文，en-us或不传表示英文

        :return: The x_language of this ListScriptsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListScriptsRequest.

        国际化标记，zh-cn表示中文，en-us或不传表示英文

        :param x_language: The x_language of this ListScriptsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def x_project_id(self):
        r"""Gets the x_project_id of this ListScriptsRequest.

        项目ID，一个项目对应一个region

        :return: The x_project_id of this ListScriptsRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        r"""Sets the x_project_id of this ListScriptsRequest.

        项目ID，一个项目对应一个region

        :param x_project_id: The x_project_id of this ListScriptsRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def x_user_profile(self):
        r"""Gets the x_user_profile of this ListScriptsRequest.

        IAM5.0用户信息

        :return: The x_user_profile of this ListScriptsRequest.
        :rtype: str
        """
        return self._x_user_profile

    @x_user_profile.setter
    def x_user_profile(self, x_user_profile):
        r"""Sets the x_user_profile of this ListScriptsRequest.

        IAM5.0用户信息

        :param x_user_profile: The x_user_profile of this ListScriptsRequest.
        :type x_user_profile: str
        """
        self._x_user_profile = x_user_profile

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
        if not isinstance(other, ListScriptsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
