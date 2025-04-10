# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetScriptJobInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execute_uuid': 'str',
        'x_language': 'str',
        'x_project_id': 'str',
        'x_user_profile': 'str'
    }

    attribute_map = {
        'execute_uuid': 'execute_uuid',
        'x_language': 'X-Language',
        'x_project_id': 'x-project-id',
        'x_user_profile': 'x-user-profile'
    }

    def __init__(self, execute_uuid=None, x_language=None, x_project_id=None, x_user_profile=None):
        r"""GetScriptJobInfoRequest

        The model defined in huaweicloud sdk

        :param execute_uuid: 脚本工单的执行Id，取自executeJobScript和ListJobScriptOrders返回体中
        :type execute_uuid: str
        :param x_language: 国际化标记，zh-cn表示中文，en-us或不传表示英文
        :type x_language: str
        :param x_project_id: 项目ID，一个项目对应一个region
        :type x_project_id: str
        :param x_user_profile: IAM5.0用户信息
        :type x_user_profile: str
        """
        
        

        self._execute_uuid = None
        self._x_language = None
        self._x_project_id = None
        self._x_user_profile = None
        self.discriminator = None

        self.execute_uuid = execute_uuid
        if x_language is not None:
            self.x_language = x_language
        if x_project_id is not None:
            self.x_project_id = x_project_id
        if x_user_profile is not None:
            self.x_user_profile = x_user_profile

    @property
    def execute_uuid(self):
        r"""Gets the execute_uuid of this GetScriptJobInfoRequest.

        脚本工单的执行Id，取自executeJobScript和ListJobScriptOrders返回体中

        :return: The execute_uuid of this GetScriptJobInfoRequest.
        :rtype: str
        """
        return self._execute_uuid

    @execute_uuid.setter
    def execute_uuid(self, execute_uuid):
        r"""Sets the execute_uuid of this GetScriptJobInfoRequest.

        脚本工单的执行Id，取自executeJobScript和ListJobScriptOrders返回体中

        :param execute_uuid: The execute_uuid of this GetScriptJobInfoRequest.
        :type execute_uuid: str
        """
        self._execute_uuid = execute_uuid

    @property
    def x_language(self):
        r"""Gets the x_language of this GetScriptJobInfoRequest.

        国际化标记，zh-cn表示中文，en-us或不传表示英文

        :return: The x_language of this GetScriptJobInfoRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this GetScriptJobInfoRequest.

        国际化标记，zh-cn表示中文，en-us或不传表示英文

        :param x_language: The x_language of this GetScriptJobInfoRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def x_project_id(self):
        r"""Gets the x_project_id of this GetScriptJobInfoRequest.

        项目ID，一个项目对应一个region

        :return: The x_project_id of this GetScriptJobInfoRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        r"""Sets the x_project_id of this GetScriptJobInfoRequest.

        项目ID，一个项目对应一个region

        :param x_project_id: The x_project_id of this GetScriptJobInfoRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def x_user_profile(self):
        r"""Gets the x_user_profile of this GetScriptJobInfoRequest.

        IAM5.0用户信息

        :return: The x_user_profile of this GetScriptJobInfoRequest.
        :rtype: str
        """
        return self._x_user_profile

    @x_user_profile.setter
    def x_user_profile(self, x_user_profile):
        r"""Sets the x_user_profile of this GetScriptJobInfoRequest.

        IAM5.0用户信息

        :param x_user_profile: The x_user_profile of this GetScriptJobInfoRequest.
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
        if not isinstance(other, GetScriptJobInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
