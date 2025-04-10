# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAppInstanceResponse(SdkResponse):

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
        'namespace': 'str',
        'version': 'str',
        'app_id': 'str',
        'app_version': 'str',
        'status': 'str',
        'status_description': 'str',
        'values': 'object',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'namespace': 'namespace',
        'version': 'version',
        'app_id': 'app_id',
        'app_version': 'app_version',
        'status': 'status',
        'status_description': 'status_description',
        'values': 'values',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, namespace=None, version=None, app_id=None, app_version=None, status=None, status_description=None, values=None, create_time=None, update_time=None):
        r"""UpdateAppInstanceResponse

        The model defined in huaweicloud sdk

        :param id: 应用实例ID
        :type id: str
        :param namespace: 边缘集群命名空间
        :type namespace: str
        :param version: 应用实例版本
        :type version: str
        :param app_id: 应用ID
        :type app_id: str
        :param app_version: 应用版本
        :type app_version: str
        :param status: 应用实例状态
        :type status: str
        :param status_description: 状态描述
        :type status_description: str
        :param values: 应用实例chart配置
        :type values: object
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 最后一次更新时间
        :type update_time: str
        """
        
        super(UpdateAppInstanceResponse, self).__init__()

        self._id = None
        self._namespace = None
        self._version = None
        self._app_id = None
        self._app_version = None
        self._status = None
        self._status_description = None
        self._values = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if namespace is not None:
            self.namespace = namespace
        if version is not None:
            self.version = version
        if app_id is not None:
            self.app_id = app_id
        if app_version is not None:
            self.app_version = app_version
        if status is not None:
            self.status = status
        if status_description is not None:
            self.status_description = status_description
        if values is not None:
            self.values = values
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this UpdateAppInstanceResponse.

        应用实例ID

        :return: The id of this UpdateAppInstanceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateAppInstanceResponse.

        应用实例ID

        :param id: The id of this UpdateAppInstanceResponse.
        :type id: str
        """
        self._id = id

    @property
    def namespace(self):
        r"""Gets the namespace of this UpdateAppInstanceResponse.

        边缘集群命名空间

        :return: The namespace of this UpdateAppInstanceResponse.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this UpdateAppInstanceResponse.

        边缘集群命名空间

        :param namespace: The namespace of this UpdateAppInstanceResponse.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def version(self):
        r"""Gets the version of this UpdateAppInstanceResponse.

        应用实例版本

        :return: The version of this UpdateAppInstanceResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this UpdateAppInstanceResponse.

        应用实例版本

        :param version: The version of this UpdateAppInstanceResponse.
        :type version: str
        """
        self._version = version

    @property
    def app_id(self):
        r"""Gets the app_id of this UpdateAppInstanceResponse.

        应用ID

        :return: The app_id of this UpdateAppInstanceResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this UpdateAppInstanceResponse.

        应用ID

        :param app_id: The app_id of this UpdateAppInstanceResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_version(self):
        r"""Gets the app_version of this UpdateAppInstanceResponse.

        应用版本

        :return: The app_version of this UpdateAppInstanceResponse.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        r"""Sets the app_version of this UpdateAppInstanceResponse.

        应用版本

        :param app_version: The app_version of this UpdateAppInstanceResponse.
        :type app_version: str
        """
        self._app_version = app_version

    @property
    def status(self):
        r"""Gets the status of this UpdateAppInstanceResponse.

        应用实例状态

        :return: The status of this UpdateAppInstanceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateAppInstanceResponse.

        应用实例状态

        :param status: The status of this UpdateAppInstanceResponse.
        :type status: str
        """
        self._status = status

    @property
    def status_description(self):
        r"""Gets the status_description of this UpdateAppInstanceResponse.

        状态描述

        :return: The status_description of this UpdateAppInstanceResponse.
        :rtype: str
        """
        return self._status_description

    @status_description.setter
    def status_description(self, status_description):
        r"""Sets the status_description of this UpdateAppInstanceResponse.

        状态描述

        :param status_description: The status_description of this UpdateAppInstanceResponse.
        :type status_description: str
        """
        self._status_description = status_description

    @property
    def values(self):
        r"""Gets the values of this UpdateAppInstanceResponse.

        应用实例chart配置

        :return: The values of this UpdateAppInstanceResponse.
        :rtype: object
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this UpdateAppInstanceResponse.

        应用实例chart配置

        :param values: The values of this UpdateAppInstanceResponse.
        :type values: object
        """
        self._values = values

    @property
    def create_time(self):
        r"""Gets the create_time of this UpdateAppInstanceResponse.

        创建时间

        :return: The create_time of this UpdateAppInstanceResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this UpdateAppInstanceResponse.

        创建时间

        :param create_time: The create_time of this UpdateAppInstanceResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this UpdateAppInstanceResponse.

        最后一次更新时间

        :return: The update_time of this UpdateAppInstanceResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this UpdateAppInstanceResponse.

        最后一次更新时间

        :param update_time: The update_time of this UpdateAppInstanceResponse.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, UpdateAppInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
