# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeystoneCreateProjectOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'parent_id': 'str',
        'domain_id': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'parent_id': 'parent_id',
        'domain_id': 'domain_id',
        'description': 'description'
    }

    def __init__(self, name=None, parent_id=None, domain_id=None, description=None):
        """KeystoneCreateProjectOption

        The model defined in huaweicloud sdk

        :param name: 项目名称。必须以存在的\&quot;区域ID_\&quot;开头，长度小于等于64字符。例如区域“华北-北京一”的区域ID为“cn-north-1”，在其下创建项目时，项目名应填“cn-north-1_IAMProject”
        :type name: str
        :param parent_id: 区域对应的项目ID，例如区域“华北-北京一”区域对应的项目ID为：04dd42abe48026ad2fa3c01ad7fa.....，获取方式请参见：[获取账号、IAM用户、项目、用户组、委托的名称和ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。
        :type parent_id: str
        :param domain_id: 项目所属账号ID。
        :type domain_id: str
        :param description: 项目描述信息，长度小于等于255字符。
        :type description: str
        """
        
        

        self._name = None
        self._parent_id = None
        self._domain_id = None
        self._description = None
        self.discriminator = None

        self.name = name
        self.parent_id = parent_id
        if domain_id is not None:
            self.domain_id = domain_id
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this KeystoneCreateProjectOption.

        项目名称。必须以存在的\"区域ID_\"开头，长度小于等于64字符。例如区域“华北-北京一”的区域ID为“cn-north-1”，在其下创建项目时，项目名应填“cn-north-1_IAMProject”

        :return: The name of this KeystoneCreateProjectOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this KeystoneCreateProjectOption.

        项目名称。必须以存在的\"区域ID_\"开头，长度小于等于64字符。例如区域“华北-北京一”的区域ID为“cn-north-1”，在其下创建项目时，项目名应填“cn-north-1_IAMProject”

        :param name: The name of this KeystoneCreateProjectOption.
        :type name: str
        """
        self._name = name

    @property
    def parent_id(self):
        """Gets the parent_id of this KeystoneCreateProjectOption.

        区域对应的项目ID，例如区域“华北-北京一”区域对应的项目ID为：04dd42abe48026ad2fa3c01ad7fa.....，获取方式请参见：[获取账号、IAM用户、项目、用户组、委托的名称和ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。

        :return: The parent_id of this KeystoneCreateProjectOption.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this KeystoneCreateProjectOption.

        区域对应的项目ID，例如区域“华北-北京一”区域对应的项目ID为：04dd42abe48026ad2fa3c01ad7fa.....，获取方式请参见：[获取账号、IAM用户、项目、用户组、委托的名称和ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。

        :param parent_id: The parent_id of this KeystoneCreateProjectOption.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def domain_id(self):
        """Gets the domain_id of this KeystoneCreateProjectOption.

        项目所属账号ID。

        :return: The domain_id of this KeystoneCreateProjectOption.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this KeystoneCreateProjectOption.

        项目所属账号ID。

        :param domain_id: The domain_id of this KeystoneCreateProjectOption.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def description(self):
        """Gets the description of this KeystoneCreateProjectOption.

        项目描述信息，长度小于等于255字符。

        :return: The description of this KeystoneCreateProjectOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this KeystoneCreateProjectOption.

        项目描述信息，长度小于等于255字符。

        :param description: The description of this KeystoneCreateProjectOption.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, KeystoneCreateProjectOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
