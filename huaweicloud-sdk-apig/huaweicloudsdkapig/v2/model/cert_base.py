# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CertBase:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'instance_id': 'str',
        'project_id': 'str',
        'common_name': 'str',
        'san': 'list[str]',
        'not_after': 'datetime',
        'signature_algorithm': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'is_has_trusted_root_ca': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'instance_id': 'instance_id',
        'project_id': 'project_id',
        'common_name': 'common_name',
        'san': 'san',
        'not_after': 'not_after',
        'signature_algorithm': 'signature_algorithm',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'is_has_trusted_root_ca': 'is_has_trusted_root_ca'
    }

    def __init__(self, id=None, name=None, type=None, instance_id=None, project_id=None, common_name=None, san=None, not_after=None, signature_algorithm=None, create_time=None, update_time=None, is_has_trusted_root_ca=None):
        """CertBase

        The model defined in huaweicloud sdk

        :param id: 证书ID
        :type id: str
        :param name: 证书名称
        :type name: str
        :param type: 证书类型  - global：全局证书 - instance：实例证书
        :type type: str
        :param instance_id: 实例编码  - &#x60;type&#x60;为&#x60;global&#x60;时，缺省为common - &#x60;type&#x60;为&#x60;instance&#x60;时，为实例编码
        :type instance_id: str
        :param project_id: 租户项目编号
        :type project_id: str
        :param common_name: 域名
        :type common_name: str
        :param san: san扩展域名
        :type san: list[str]
        :param not_after: 有效期到
        :type not_after: datetime
        :param signature_algorithm: 签名算法
        :type signature_algorithm: str
        :param create_time: 创建时间
        :type create_time: datetime
        :param update_time: 更新时间
        :type update_time: datetime
        :param is_has_trusted_root_ca: 是否存在信任的根证书CA。当绑定证书存在trusted_root_ca时为true。
        :type is_has_trusted_root_ca: bool
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._instance_id = None
        self._project_id = None
        self._common_name = None
        self._san = None
        self._not_after = None
        self._signature_algorithm = None
        self._create_time = None
        self._update_time = None
        self._is_has_trusted_root_ca = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if instance_id is not None:
            self.instance_id = instance_id
        if project_id is not None:
            self.project_id = project_id
        if common_name is not None:
            self.common_name = common_name
        if san is not None:
            self.san = san
        if not_after is not None:
            self.not_after = not_after
        if signature_algorithm is not None:
            self.signature_algorithm = signature_algorithm
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if is_has_trusted_root_ca is not None:
            self.is_has_trusted_root_ca = is_has_trusted_root_ca

    @property
    def id(self):
        """Gets the id of this CertBase.

        证书ID

        :return: The id of this CertBase.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CertBase.

        证书ID

        :param id: The id of this CertBase.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CertBase.

        证书名称

        :return: The name of this CertBase.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CertBase.

        证书名称

        :param name: The name of this CertBase.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this CertBase.

        证书类型  - global：全局证书 - instance：实例证书

        :return: The type of this CertBase.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CertBase.

        证书类型  - global：全局证书 - instance：实例证书

        :param type: The type of this CertBase.
        :type type: str
        """
        self._type = type

    @property
    def instance_id(self):
        """Gets the instance_id of this CertBase.

        实例编码  - `type`为`global`时，缺省为common - `type`为`instance`时，为实例编码

        :return: The instance_id of this CertBase.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CertBase.

        实例编码  - `type`为`global`时，缺省为common - `type`为`instance`时，为实例编码

        :param instance_id: The instance_id of this CertBase.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def project_id(self):
        """Gets the project_id of this CertBase.

        租户项目编号

        :return: The project_id of this CertBase.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CertBase.

        租户项目编号

        :param project_id: The project_id of this CertBase.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def common_name(self):
        """Gets the common_name of this CertBase.

        域名

        :return: The common_name of this CertBase.
        :rtype: str
        """
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        """Sets the common_name of this CertBase.

        域名

        :param common_name: The common_name of this CertBase.
        :type common_name: str
        """
        self._common_name = common_name

    @property
    def san(self):
        """Gets the san of this CertBase.

        san扩展域名

        :return: The san of this CertBase.
        :rtype: list[str]
        """
        return self._san

    @san.setter
    def san(self, san):
        """Sets the san of this CertBase.

        san扩展域名

        :param san: The san of this CertBase.
        :type san: list[str]
        """
        self._san = san

    @property
    def not_after(self):
        """Gets the not_after of this CertBase.

        有效期到

        :return: The not_after of this CertBase.
        :rtype: datetime
        """
        return self._not_after

    @not_after.setter
    def not_after(self, not_after):
        """Sets the not_after of this CertBase.

        有效期到

        :param not_after: The not_after of this CertBase.
        :type not_after: datetime
        """
        self._not_after = not_after

    @property
    def signature_algorithm(self):
        """Gets the signature_algorithm of this CertBase.

        签名算法

        :return: The signature_algorithm of this CertBase.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        """Sets the signature_algorithm of this CertBase.

        签名算法

        :param signature_algorithm: The signature_algorithm of this CertBase.
        :type signature_algorithm: str
        """
        self._signature_algorithm = signature_algorithm

    @property
    def create_time(self):
        """Gets the create_time of this CertBase.

        创建时间

        :return: The create_time of this CertBase.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CertBase.

        创建时间

        :param create_time: The create_time of this CertBase.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this CertBase.

        更新时间

        :return: The update_time of this CertBase.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this CertBase.

        更新时间

        :param update_time: The update_time of this CertBase.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def is_has_trusted_root_ca(self):
        """Gets the is_has_trusted_root_ca of this CertBase.

        是否存在信任的根证书CA。当绑定证书存在trusted_root_ca时为true。

        :return: The is_has_trusted_root_ca of this CertBase.
        :rtype: bool
        """
        return self._is_has_trusted_root_ca

    @is_has_trusted_root_ca.setter
    def is_has_trusted_root_ca(self, is_has_trusted_root_ca):
        """Sets the is_has_trusted_root_ca of this CertBase.

        是否存在信任的根证书CA。当绑定证书存在trusted_root_ca时为true。

        :param is_has_trusted_root_ca: The is_has_trusted_root_ca of this CertBase.
        :type is_has_trusted_root_ca: bool
        """
        self._is_has_trusted_root_ca = is_has_trusted_root_ca

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
        if not isinstance(other, CertBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
