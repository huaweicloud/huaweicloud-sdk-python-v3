# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowServerResponse(SdkResponse):

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
        'project_id': 'str',
        'domain_id': 'str',
        'manage_state': 'ManageState',
        'power_state': 'PowerState',
        'health_state': 'Health',
        'onboard_time': 'str',
        'location': 'Location',
        'hardware_attributes': 'HardwareSummary',
        'tags': 'list[Tag]',
        'error': 'ErrorStatus'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'project_id': 'project_id',
        'domain_id': 'domain_id',
        'manage_state': 'manage_state',
        'power_state': 'power_state',
        'health_state': 'health_state',
        'onboard_time': 'onboard_time',
        'location': 'location',
        'hardware_attributes': 'hardware_attributes',
        'tags': 'tags',
        'error': 'error'
    }

    def __init__(self, id=None, name=None, project_id=None, domain_id=None, manage_state=None, power_state=None, health_state=None, onboard_time=None, location=None, hardware_attributes=None, tags=None, error=None):
        r"""ShowServerResponse

        The model defined in huaweicloud sdk

        :param id: UUID（Universally Unique Identifier）是一个 128 位的数字，通常以 32 个十六进制数字的形式表示，分为 5 组，用连字符分隔。具体格式如下：  xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx 其中：  每个 x 是一个十六进制数字（0-9 或 a-f）。 5 组的长度分别是：8 位、4 位、4 位、4 位 和 12 位。 为了匹配这种格式的 UUID，可以使用以下正则表达式：  regex ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
        :type id: str
        :param name: Resource Name Type
        :type name: str
        :param project_id: project id
        :type project_id: str
        :param domain_id: domain id
        :type domain_id: str
        :param manage_state: 
        :type manage_state: :class:`huaweicloudsdkclouddc.v1.ManageState`
        :param power_state: 
        :type power_state: :class:`huaweicloudsdkclouddc.v1.PowerState`
        :param health_state: 
        :type health_state: :class:`huaweicloudsdkclouddc.v1.Health`
        :param onboard_time: 上架时间
        :type onboard_time: str
        :param location: 
        :type location: :class:`huaweicloudsdkclouddc.v1.Location`
        :param hardware_attributes: 
        :type hardware_attributes: :class:`huaweicloudsdkclouddc.v1.HardwareSummary`
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkclouddc.v1.Tag`]
        :param error: 
        :type error: :class:`huaweicloudsdkclouddc.v1.ErrorStatus`
        """
        
        super(ShowServerResponse, self).__init__()

        self._id = None
        self._name = None
        self._project_id = None
        self._domain_id = None
        self._manage_state = None
        self._power_state = None
        self._health_state = None
        self._onboard_time = None
        self._location = None
        self._hardware_attributes = None
        self._tags = None
        self._error = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if domain_id is not None:
            self.domain_id = domain_id
        if manage_state is not None:
            self.manage_state = manage_state
        if power_state is not None:
            self.power_state = power_state
        if health_state is not None:
            self.health_state = health_state
        if onboard_time is not None:
            self.onboard_time = onboard_time
        if location is not None:
            self.location = location
        if hardware_attributes is not None:
            self.hardware_attributes = hardware_attributes
        if tags is not None:
            self.tags = tags
        if error is not None:
            self.error = error

    @property
    def id(self):
        r"""Gets the id of this ShowServerResponse.

        UUID（Universally Unique Identifier）是一个 128 位的数字，通常以 32 个十六进制数字的形式表示，分为 5 组，用连字符分隔。具体格式如下：  xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx 其中：  每个 x 是一个十六进制数字（0-9 或 a-f）。 5 组的长度分别是：8 位、4 位、4 位、4 位 和 12 位。 为了匹配这种格式的 UUID，可以使用以下正则表达式：  regex ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$

        :return: The id of this ShowServerResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowServerResponse.

        UUID（Universally Unique Identifier）是一个 128 位的数字，通常以 32 个十六进制数字的形式表示，分为 5 组，用连字符分隔。具体格式如下：  xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx 其中：  每个 x 是一个十六进制数字（0-9 或 a-f）。 5 组的长度分别是：8 位、4 位、4 位、4 位 和 12 位。 为了匹配这种格式的 UUID，可以使用以下正则表达式：  regex ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$

        :param id: The id of this ShowServerResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowServerResponse.

        Resource Name Type

        :return: The name of this ShowServerResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowServerResponse.

        Resource Name Type

        :param name: The name of this ShowServerResponse.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowServerResponse.

        project id

        :return: The project_id of this ShowServerResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowServerResponse.

        project id

        :param project_id: The project_id of this ShowServerResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowServerResponse.

        domain id

        :return: The domain_id of this ShowServerResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowServerResponse.

        domain id

        :param domain_id: The domain_id of this ShowServerResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def manage_state(self):
        r"""Gets the manage_state of this ShowServerResponse.

        :return: The manage_state of this ShowServerResponse.
        :rtype: :class:`huaweicloudsdkclouddc.v1.ManageState`
        """
        return self._manage_state

    @manage_state.setter
    def manage_state(self, manage_state):
        r"""Sets the manage_state of this ShowServerResponse.

        :param manage_state: The manage_state of this ShowServerResponse.
        :type manage_state: :class:`huaweicloudsdkclouddc.v1.ManageState`
        """
        self._manage_state = manage_state

    @property
    def power_state(self):
        r"""Gets the power_state of this ShowServerResponse.

        :return: The power_state of this ShowServerResponse.
        :rtype: :class:`huaweicloudsdkclouddc.v1.PowerState`
        """
        return self._power_state

    @power_state.setter
    def power_state(self, power_state):
        r"""Sets the power_state of this ShowServerResponse.

        :param power_state: The power_state of this ShowServerResponse.
        :type power_state: :class:`huaweicloudsdkclouddc.v1.PowerState`
        """
        self._power_state = power_state

    @property
    def health_state(self):
        r"""Gets the health_state of this ShowServerResponse.

        :return: The health_state of this ShowServerResponse.
        :rtype: :class:`huaweicloudsdkclouddc.v1.Health`
        """
        return self._health_state

    @health_state.setter
    def health_state(self, health_state):
        r"""Sets the health_state of this ShowServerResponse.

        :param health_state: The health_state of this ShowServerResponse.
        :type health_state: :class:`huaweicloudsdkclouddc.v1.Health`
        """
        self._health_state = health_state

    @property
    def onboard_time(self):
        r"""Gets the onboard_time of this ShowServerResponse.

        上架时间

        :return: The onboard_time of this ShowServerResponse.
        :rtype: str
        """
        return self._onboard_time

    @onboard_time.setter
    def onboard_time(self, onboard_time):
        r"""Sets the onboard_time of this ShowServerResponse.

        上架时间

        :param onboard_time: The onboard_time of this ShowServerResponse.
        :type onboard_time: str
        """
        self._onboard_time = onboard_time

    @property
    def location(self):
        r"""Gets the location of this ShowServerResponse.

        :return: The location of this ShowServerResponse.
        :rtype: :class:`huaweicloudsdkclouddc.v1.Location`
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this ShowServerResponse.

        :param location: The location of this ShowServerResponse.
        :type location: :class:`huaweicloudsdkclouddc.v1.Location`
        """
        self._location = location

    @property
    def hardware_attributes(self):
        r"""Gets the hardware_attributes of this ShowServerResponse.

        :return: The hardware_attributes of this ShowServerResponse.
        :rtype: :class:`huaweicloudsdkclouddc.v1.HardwareSummary`
        """
        return self._hardware_attributes

    @hardware_attributes.setter
    def hardware_attributes(self, hardware_attributes):
        r"""Sets the hardware_attributes of this ShowServerResponse.

        :param hardware_attributes: The hardware_attributes of this ShowServerResponse.
        :type hardware_attributes: :class:`huaweicloudsdkclouddc.v1.HardwareSummary`
        """
        self._hardware_attributes = hardware_attributes

    @property
    def tags(self):
        r"""Gets the tags of this ShowServerResponse.

        标签

        :return: The tags of this ShowServerResponse.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ShowServerResponse.

        标签

        :param tags: The tags of this ShowServerResponse.
        :type tags: list[:class:`huaweicloudsdkclouddc.v1.Tag`]
        """
        self._tags = tags

    @property
    def error(self):
        r"""Gets the error of this ShowServerResponse.

        :return: The error of this ShowServerResponse.
        :rtype: :class:`huaweicloudsdkclouddc.v1.ErrorStatus`
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this ShowServerResponse.

        :param error: The error of this ShowServerResponse.
        :type error: :class:`huaweicloudsdkclouddc.v1.ErrorStatus`
        """
        self._error = error

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
        if not isinstance(other, ShowServerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
