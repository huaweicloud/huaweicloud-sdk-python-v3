# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMultiCloudClusterImageCommandRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('password')

    openapi_types = {
        'image_repo': 'str',
        'organization': 'str',
        'username': 'str',
        'password': 'str',
        'plug_type': 'str'
    }

    attribute_map = {
        'image_repo': 'image_repo',
        'organization': 'organization',
        'username': 'username',
        'password': 'password',
        'plug_type': 'plug_type'
    }

    def __init__(self, image_repo=None, organization=None, username=None, password=None, plug_type=None):
        r"""ShowMultiCloudClusterImageCommandRequest

        The model defined in huaweicloud sdk

        :param image_repo: 镜像仓地址
        :type image_repo: str
        :param organization: 组织名称
        :type organization: str
        :param username: 用户名
        :type username: str
        :param password: 密码
        :type password: str
        :param plug_type: **参数解释**: 插件类型 **约束限制**: 不涉及 **取值范围**: - docker: docker插件镜像 - agent: hostguard镜像 **默认取值**: 不涉及 
        :type plug_type: str
        """
        
        

        self._image_repo = None
        self._organization = None
        self._username = None
        self._password = None
        self._plug_type = None
        self.discriminator = None

        self.image_repo = image_repo
        self.organization = organization
        self.username = username
        self.password = password
        if plug_type is not None:
            self.plug_type = plug_type

    @property
    def image_repo(self):
        r"""Gets the image_repo of this ShowMultiCloudClusterImageCommandRequest.

        镜像仓地址

        :return: The image_repo of this ShowMultiCloudClusterImageCommandRequest.
        :rtype: str
        """
        return self._image_repo

    @image_repo.setter
    def image_repo(self, image_repo):
        r"""Sets the image_repo of this ShowMultiCloudClusterImageCommandRequest.

        镜像仓地址

        :param image_repo: The image_repo of this ShowMultiCloudClusterImageCommandRequest.
        :type image_repo: str
        """
        self._image_repo = image_repo

    @property
    def organization(self):
        r"""Gets the organization of this ShowMultiCloudClusterImageCommandRequest.

        组织名称

        :return: The organization of this ShowMultiCloudClusterImageCommandRequest.
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        r"""Sets the organization of this ShowMultiCloudClusterImageCommandRequest.

        组织名称

        :param organization: The organization of this ShowMultiCloudClusterImageCommandRequest.
        :type organization: str
        """
        self._organization = organization

    @property
    def username(self):
        r"""Gets the username of this ShowMultiCloudClusterImageCommandRequest.

        用户名

        :return: The username of this ShowMultiCloudClusterImageCommandRequest.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this ShowMultiCloudClusterImageCommandRequest.

        用户名

        :param username: The username of this ShowMultiCloudClusterImageCommandRequest.
        :type username: str
        """
        self._username = username

    @property
    def password(self):
        r"""Gets the password of this ShowMultiCloudClusterImageCommandRequest.

        密码

        :return: The password of this ShowMultiCloudClusterImageCommandRequest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this ShowMultiCloudClusterImageCommandRequest.

        密码

        :param password: The password of this ShowMultiCloudClusterImageCommandRequest.
        :type password: str
        """
        self._password = password

    @property
    def plug_type(self):
        r"""Gets the plug_type of this ShowMultiCloudClusterImageCommandRequest.

        **参数解释**: 插件类型 **约束限制**: 不涉及 **取值范围**: - docker: docker插件镜像 - agent: hostguard镜像 **默认取值**: 不涉及 

        :return: The plug_type of this ShowMultiCloudClusterImageCommandRequest.
        :rtype: str
        """
        return self._plug_type

    @plug_type.setter
    def plug_type(self, plug_type):
        r"""Sets the plug_type of this ShowMultiCloudClusterImageCommandRequest.

        **参数解释**: 插件类型 **约束限制**: 不涉及 **取值范围**: - docker: docker插件镜像 - agent: hostguard镜像 **默认取值**: 不涉及 

        :param plug_type: The plug_type of this ShowMultiCloudClusterImageCommandRequest.
        :type plug_type: str
        """
        self._plug_type = plug_type

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
        if not isinstance(other, ShowMultiCloudClusterImageCommandRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
