# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Registry:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'description': 'str',
        'region_id': 'str',
        'instance_id': 'str',
        'type': 'str',
        'url': 'str',
        'credential': 'Credential',
        'insecure': 'bool',
        'status': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'region_id': 'region_id',
        'instance_id': 'instance_id',
        'type': 'type',
        'url': 'url',
        'credential': 'credential',
        'insecure': 'insecure',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, description=None, region_id=None, instance_id=None, type=None, url=None, credential=None, insecure=None, status=None, created_at=None, updated_at=None):
        r"""Registry

        The model defined in huaweicloud sdk

        :param id: 仓库ID
        :type id: int
        :param name: 仓库名称
        :type name: str
        :param description: 仓库描述
        :type description: str
        :param region_id: 区域ID
        :type region_id: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param type: 仓库类型
        :type type: str
        :param url: 仓库地址
        :type url: str
        :param credential: 
        :type credential: :class:`huaweicloudsdkswr.v2.Credential`
        :param insecure: 是否验证远程证书
        :type insecure: bool
        :param status: 仓库状态，healthy或unhealthy
        :type status: str
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._region_id = None
        self._instance_id = None
        self._type = None
        self._url = None
        self._credential = None
        self._insecure = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if region_id is not None:
            self.region_id = region_id
        if instance_id is not None:
            self.instance_id = instance_id
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url
        if credential is not None:
            self.credential = credential
        if insecure is not None:
            self.insecure = insecure
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this Registry.

        仓库ID

        :return: The id of this Registry.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Registry.

        仓库ID

        :param id: The id of this Registry.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this Registry.

        仓库名称

        :return: The name of this Registry.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Registry.

        仓库名称

        :param name: The name of this Registry.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this Registry.

        仓库描述

        :return: The description of this Registry.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Registry.

        仓库描述

        :param description: The description of this Registry.
        :type description: str
        """
        self._description = description

    @property
    def region_id(self):
        r"""Gets the region_id of this Registry.

        区域ID

        :return: The region_id of this Registry.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this Registry.

        区域ID

        :param region_id: The region_id of this Registry.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this Registry.

        实例ID

        :return: The instance_id of this Registry.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this Registry.

        实例ID

        :param instance_id: The instance_id of this Registry.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def type(self):
        r"""Gets the type of this Registry.

        仓库类型

        :return: The type of this Registry.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Registry.

        仓库类型

        :param type: The type of this Registry.
        :type type: str
        """
        self._type = type

    @property
    def url(self):
        r"""Gets the url of this Registry.

        仓库地址

        :return: The url of this Registry.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this Registry.

        仓库地址

        :param url: The url of this Registry.
        :type url: str
        """
        self._url = url

    @property
    def credential(self):
        r"""Gets the credential of this Registry.

        :return: The credential of this Registry.
        :rtype: :class:`huaweicloudsdkswr.v2.Credential`
        """
        return self._credential

    @credential.setter
    def credential(self, credential):
        r"""Sets the credential of this Registry.

        :param credential: The credential of this Registry.
        :type credential: :class:`huaweicloudsdkswr.v2.Credential`
        """
        self._credential = credential

    @property
    def insecure(self):
        r"""Gets the insecure of this Registry.

        是否验证远程证书

        :return: The insecure of this Registry.
        :rtype: bool
        """
        return self._insecure

    @insecure.setter
    def insecure(self, insecure):
        r"""Sets the insecure of this Registry.

        是否验证远程证书

        :param insecure: The insecure of this Registry.
        :type insecure: bool
        """
        self._insecure = insecure

    @property
    def status(self):
        r"""Gets the status of this Registry.

        仓库状态，healthy或unhealthy

        :return: The status of this Registry.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Registry.

        仓库状态，healthy或unhealthy

        :param status: The status of this Registry.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this Registry.

        创建时间

        :return: The created_at of this Registry.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this Registry.

        创建时间

        :param created_at: The created_at of this Registry.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this Registry.

        更新时间

        :return: The updated_at of this Registry.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this Registry.

        更新时间

        :param updated_at: The updated_at of this Registry.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, Registry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
