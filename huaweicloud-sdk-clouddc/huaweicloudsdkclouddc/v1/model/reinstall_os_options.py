# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReinstallOSOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_id': 'str',
        'password': 'str',
        'instance_id_set': 'list[str]'
    }

    attribute_map = {
        'image_id': 'image_id',
        'password': 'password',
        'instance_id_set': 'instance_id_set'
    }

    def __init__(self, image_id=None, password=None, instance_id_set=None):
        r"""ReinstallOSOptions

        The model defined in huaweicloud sdk

        :param image_id: 镜像ID，非必填，不传默认使用当前镜像ID
        :type image_id: str
        :param password: 设置实例的管理员账户初始登录密码，其中，Linux管理员账户为root，Windows管理员账户为Administrator。
        :type password: str
        :param instance_id_set: **参数解释**： 实例id 列表 **约束限制**： 实例id不超过10条 
        :type instance_id_set: list[str]
        """
        
        

        self._image_id = None
        self._password = None
        self._instance_id_set = None
        self.discriminator = None

        if image_id is not None:
            self.image_id = image_id
        self.password = password
        if instance_id_set is not None:
            self.instance_id_set = instance_id_set

    @property
    def image_id(self):
        r"""Gets the image_id of this ReinstallOSOptions.

        镜像ID，非必填，不传默认使用当前镜像ID

        :return: The image_id of this ReinstallOSOptions.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ReinstallOSOptions.

        镜像ID，非必填，不传默认使用当前镜像ID

        :param image_id: The image_id of this ReinstallOSOptions.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def password(self):
        r"""Gets the password of this ReinstallOSOptions.

        设置实例的管理员账户初始登录密码，其中，Linux管理员账户为root，Windows管理员账户为Administrator。

        :return: The password of this ReinstallOSOptions.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this ReinstallOSOptions.

        设置实例的管理员账户初始登录密码，其中，Linux管理员账户为root，Windows管理员账户为Administrator。

        :param password: The password of this ReinstallOSOptions.
        :type password: str
        """
        self._password = password

    @property
    def instance_id_set(self):
        r"""Gets the instance_id_set of this ReinstallOSOptions.

        **参数解释**： 实例id 列表 **约束限制**： 实例id不超过10条 

        :return: The instance_id_set of this ReinstallOSOptions.
        :rtype: list[str]
        """
        return self._instance_id_set

    @instance_id_set.setter
    def instance_id_set(self, instance_id_set):
        r"""Sets the instance_id_set of this ReinstallOSOptions.

        **参数解释**： 实例id 列表 **约束限制**： 实例id不超过10条 

        :param instance_id_set: The instance_id_set of this ReinstallOSOptions.
        :type instance_id_set: list[str]
        """
        self._instance_id_set = instance_id_set

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
        if not isinstance(other, ReinstallOSOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
