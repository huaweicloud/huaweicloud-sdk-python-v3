# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMonitorSystemResponseBodySpec:

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
        'type': 'str',
        'instrumentation': 'str',
        'access_key': 'str',
        'access_value': 'str',
        'access_token': 'str',
        'master_address': 'str',
        'apm_application': 'str',
        'version': 'str',
        'image_pull_policy': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'instrumentation': 'instrumentation',
        'access_key': 'access_key',
        'access_value': 'access_value',
        'access_token': 'access_token',
        'master_address': 'master_address',
        'apm_application': 'apm_application',
        'version': 'version',
        'image_pull_policy': 'image_pull_policy',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, type=None, instrumentation=None, access_key=None, access_value=None, access_token=None, master_address=None, apm_application=None, version=None, image_pull_policy=None, created_at=None, updated_at=None):
        r"""ShowMonitorSystemResponseBodySpec

        The model defined in huaweicloud sdk

        :param id: 监控系统id。
        :type id: str
        :param type: 采集方式。
        :type type: str
        :param instrumentation: 探针注入方式。
        :type instrumentation: str
        :param access_key: apm2访问密钥Key。
        :type access_key: str
        :param access_value: apm2访问密钥value。
        :type access_value: str
        :param access_token: apm2 opentelemetry接入token。
        :type access_token: str
        :param master_address: 探针接入点。
        :type master_address: str
        :param apm_application: apm2应用。
        :type apm_application: str
        :param version: 增强型探针/opentelemetry探针版本。
        :type version: str
        :param image_pull_policy: 探针镜像更新策略。
        :type image_pull_policy: str
        :param created_at: 创建时间。
        :type created_at: str
        :param updated_at: 更新时间。
        :type updated_at: str
        """
        
        

        self._id = None
        self._type = None
        self._instrumentation = None
        self._access_key = None
        self._access_value = None
        self._access_token = None
        self._master_address = None
        self._apm_application = None
        self._version = None
        self._image_pull_policy = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if instrumentation is not None:
            self.instrumentation = instrumentation
        if access_key is not None:
            self.access_key = access_key
        if access_value is not None:
            self.access_value = access_value
        if access_token is not None:
            self.access_token = access_token
        if master_address is not None:
            self.master_address = master_address
        if apm_application is not None:
            self.apm_application = apm_application
        if version is not None:
            self.version = version
        if image_pull_policy is not None:
            self.image_pull_policy = image_pull_policy
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this ShowMonitorSystemResponseBodySpec.

        监控系统id。

        :return: The id of this ShowMonitorSystemResponseBodySpec.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowMonitorSystemResponseBodySpec.

        监控系统id。

        :param id: The id of this ShowMonitorSystemResponseBodySpec.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this ShowMonitorSystemResponseBodySpec.

        采集方式。

        :return: The type of this ShowMonitorSystemResponseBodySpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowMonitorSystemResponseBodySpec.

        采集方式。

        :param type: The type of this ShowMonitorSystemResponseBodySpec.
        :type type: str
        """
        self._type = type

    @property
    def instrumentation(self):
        r"""Gets the instrumentation of this ShowMonitorSystemResponseBodySpec.

        探针注入方式。

        :return: The instrumentation of this ShowMonitorSystemResponseBodySpec.
        :rtype: str
        """
        return self._instrumentation

    @instrumentation.setter
    def instrumentation(self, instrumentation):
        r"""Sets the instrumentation of this ShowMonitorSystemResponseBodySpec.

        探针注入方式。

        :param instrumentation: The instrumentation of this ShowMonitorSystemResponseBodySpec.
        :type instrumentation: str
        """
        self._instrumentation = instrumentation

    @property
    def access_key(self):
        r"""Gets the access_key of this ShowMonitorSystemResponseBodySpec.

        apm2访问密钥Key。

        :return: The access_key of this ShowMonitorSystemResponseBodySpec.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        r"""Sets the access_key of this ShowMonitorSystemResponseBodySpec.

        apm2访问密钥Key。

        :param access_key: The access_key of this ShowMonitorSystemResponseBodySpec.
        :type access_key: str
        """
        self._access_key = access_key

    @property
    def access_value(self):
        r"""Gets the access_value of this ShowMonitorSystemResponseBodySpec.

        apm2访问密钥value。

        :return: The access_value of this ShowMonitorSystemResponseBodySpec.
        :rtype: str
        """
        return self._access_value

    @access_value.setter
    def access_value(self, access_value):
        r"""Sets the access_value of this ShowMonitorSystemResponseBodySpec.

        apm2访问密钥value。

        :param access_value: The access_value of this ShowMonitorSystemResponseBodySpec.
        :type access_value: str
        """
        self._access_value = access_value

    @property
    def access_token(self):
        r"""Gets the access_token of this ShowMonitorSystemResponseBodySpec.

        apm2 opentelemetry接入token。

        :return: The access_token of this ShowMonitorSystemResponseBodySpec.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        r"""Sets the access_token of this ShowMonitorSystemResponseBodySpec.

        apm2 opentelemetry接入token。

        :param access_token: The access_token of this ShowMonitorSystemResponseBodySpec.
        :type access_token: str
        """
        self._access_token = access_token

    @property
    def master_address(self):
        r"""Gets the master_address of this ShowMonitorSystemResponseBodySpec.

        探针接入点。

        :return: The master_address of this ShowMonitorSystemResponseBodySpec.
        :rtype: str
        """
        return self._master_address

    @master_address.setter
    def master_address(self, master_address):
        r"""Sets the master_address of this ShowMonitorSystemResponseBodySpec.

        探针接入点。

        :param master_address: The master_address of this ShowMonitorSystemResponseBodySpec.
        :type master_address: str
        """
        self._master_address = master_address

    @property
    def apm_application(self):
        r"""Gets the apm_application of this ShowMonitorSystemResponseBodySpec.

        apm2应用。

        :return: The apm_application of this ShowMonitorSystemResponseBodySpec.
        :rtype: str
        """
        return self._apm_application

    @apm_application.setter
    def apm_application(self, apm_application):
        r"""Sets the apm_application of this ShowMonitorSystemResponseBodySpec.

        apm2应用。

        :param apm_application: The apm_application of this ShowMonitorSystemResponseBodySpec.
        :type apm_application: str
        """
        self._apm_application = apm_application

    @property
    def version(self):
        r"""Gets the version of this ShowMonitorSystemResponseBodySpec.

        增强型探针/opentelemetry探针版本。

        :return: The version of this ShowMonitorSystemResponseBodySpec.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowMonitorSystemResponseBodySpec.

        增强型探针/opentelemetry探针版本。

        :param version: The version of this ShowMonitorSystemResponseBodySpec.
        :type version: str
        """
        self._version = version

    @property
    def image_pull_policy(self):
        r"""Gets the image_pull_policy of this ShowMonitorSystemResponseBodySpec.

        探针镜像更新策略。

        :return: The image_pull_policy of this ShowMonitorSystemResponseBodySpec.
        :rtype: str
        """
        return self._image_pull_policy

    @image_pull_policy.setter
    def image_pull_policy(self, image_pull_policy):
        r"""Sets the image_pull_policy of this ShowMonitorSystemResponseBodySpec.

        探针镜像更新策略。

        :param image_pull_policy: The image_pull_policy of this ShowMonitorSystemResponseBodySpec.
        :type image_pull_policy: str
        """
        self._image_pull_policy = image_pull_policy

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowMonitorSystemResponseBodySpec.

        创建时间。

        :return: The created_at of this ShowMonitorSystemResponseBodySpec.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowMonitorSystemResponseBodySpec.

        创建时间。

        :param created_at: The created_at of this ShowMonitorSystemResponseBodySpec.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowMonitorSystemResponseBodySpec.

        更新时间。

        :return: The updated_at of this ShowMonitorSystemResponseBodySpec.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowMonitorSystemResponseBodySpec.

        更新时间。

        :param updated_at: The updated_at of this ShowMonitorSystemResponseBodySpec.
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
        if not isinstance(other, ShowMonitorSystemResponseBodySpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
