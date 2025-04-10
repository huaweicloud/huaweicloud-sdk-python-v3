# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentList:

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
        'labels': 'list[Label]',
        'runtime_stack': 'RuntimeStack',
        'status': 'ComponentStatusView',
        'environment_name': 'str',
        'application_name': 'str',
        'environment_id': 'str',
        'application_id': 'str',
        'id': 'str',
        'creator': 'str',
        'source': 'SourceObject',
        'version': 'str',
        'platform_type': 'str',
        'external_accesses': 'list[ExternalAccesses]'
    }

    attribute_map = {
        'name': 'name',
        'labels': 'labels',
        'runtime_stack': 'runtime_stack',
        'status': 'status',
        'environment_name': 'environment_name',
        'application_name': 'application_name',
        'environment_id': 'environment_id',
        'application_id': 'application_id',
        'id': 'id',
        'creator': 'creator',
        'source': 'source',
        'version': 'version',
        'platform_type': 'platform_type',
        'external_accesses': 'external_accesses'
    }

    def __init__(self, name=None, labels=None, runtime_stack=None, status=None, environment_name=None, application_name=None, environment_id=None, application_id=None, id=None, creator=None, source=None, version=None, platform_type=None, external_accesses=None):
        r"""ComponentList

        The model defined in huaweicloud sdk

        :param name: 
        :type name: str
        :param labels: 
        :type labels: list[:class:`huaweicloudsdkservicestage.v3.Label`]
        :param runtime_stack: 
        :type runtime_stack: :class:`huaweicloudsdkservicestage.v3.RuntimeStack`
        :param status: 
        :type status: :class:`huaweicloudsdkservicestage.v3.ComponentStatusView`
        :param environment_name: 
        :type environment_name: str
        :param application_name: 
        :type application_name: str
        :param environment_id: 
        :type environment_id: str
        :param application_id: 
        :type application_id: str
        :param id: 
        :type id: str
        :param creator: 
        :type creator: str
        :param source: 
        :type source: :class:`huaweicloudsdkservicestage.v3.SourceObject`
        :param version: 
        :type version: str
        :param platform_type: 
        :type platform_type: str
        :param external_accesses: 
        :type external_accesses: list[:class:`huaweicloudsdkservicestage.v3.ExternalAccesses`]
        """
        
        

        self._name = None
        self._labels = None
        self._runtime_stack = None
        self._status = None
        self._environment_name = None
        self._application_name = None
        self._environment_id = None
        self._application_id = None
        self._id = None
        self._creator = None
        self._source = None
        self._version = None
        self._platform_type = None
        self._external_accesses = None
        self.discriminator = None

        self.name = name
        if labels is not None:
            self.labels = labels
        if runtime_stack is not None:
            self.runtime_stack = runtime_stack
        if status is not None:
            self.status = status
        if environment_name is not None:
            self.environment_name = environment_name
        if application_name is not None:
            self.application_name = application_name
        if environment_id is not None:
            self.environment_id = environment_id
        if application_id is not None:
            self.application_id = application_id
        if id is not None:
            self.id = id
        if creator is not None:
            self.creator = creator
        self.source = source
        if version is not None:
            self.version = version
        if platform_type is not None:
            self.platform_type = platform_type
        if external_accesses is not None:
            self.external_accesses = external_accesses

    @property
    def name(self):
        r"""Gets the name of this ComponentList.

        :return: The name of this ComponentList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ComponentList.

        :param name: The name of this ComponentList.
        :type name: str
        """
        self._name = name

    @property
    def labels(self):
        r"""Gets the labels of this ComponentList.

        :return: The labels of this ComponentList.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.Label`]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ComponentList.

        :param labels: The labels of this ComponentList.
        :type labels: list[:class:`huaweicloudsdkservicestage.v3.Label`]
        """
        self._labels = labels

    @property
    def runtime_stack(self):
        r"""Gets the runtime_stack of this ComponentList.

        :return: The runtime_stack of this ComponentList.
        :rtype: :class:`huaweicloudsdkservicestage.v3.RuntimeStack`
        """
        return self._runtime_stack

    @runtime_stack.setter
    def runtime_stack(self, runtime_stack):
        r"""Sets the runtime_stack of this ComponentList.

        :param runtime_stack: The runtime_stack of this ComponentList.
        :type runtime_stack: :class:`huaweicloudsdkservicestage.v3.RuntimeStack`
        """
        self._runtime_stack = runtime_stack

    @property
    def status(self):
        r"""Gets the status of this ComponentList.

        :return: The status of this ComponentList.
        :rtype: :class:`huaweicloudsdkservicestage.v3.ComponentStatusView`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ComponentList.

        :param status: The status of this ComponentList.
        :type status: :class:`huaweicloudsdkservicestage.v3.ComponentStatusView`
        """
        self._status = status

    @property
    def environment_name(self):
        r"""Gets the environment_name of this ComponentList.

        :return: The environment_name of this ComponentList.
        :rtype: str
        """
        return self._environment_name

    @environment_name.setter
    def environment_name(self, environment_name):
        r"""Sets the environment_name of this ComponentList.

        :param environment_name: The environment_name of this ComponentList.
        :type environment_name: str
        """
        self._environment_name = environment_name

    @property
    def application_name(self):
        r"""Gets the application_name of this ComponentList.

        :return: The application_name of this ComponentList.
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        r"""Sets the application_name of this ComponentList.

        :param application_name: The application_name of this ComponentList.
        :type application_name: str
        """
        self._application_name = application_name

    @property
    def environment_id(self):
        r"""Gets the environment_id of this ComponentList.

        :return: The environment_id of this ComponentList.
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        r"""Sets the environment_id of this ComponentList.

        :param environment_id: The environment_id of this ComponentList.
        :type environment_id: str
        """
        self._environment_id = environment_id

    @property
    def application_id(self):
        r"""Gets the application_id of this ComponentList.

        :return: The application_id of this ComponentList.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this ComponentList.

        :param application_id: The application_id of this ComponentList.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def id(self):
        r"""Gets the id of this ComponentList.

        :return: The id of this ComponentList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ComponentList.

        :param id: The id of this ComponentList.
        :type id: str
        """
        self._id = id

    @property
    def creator(self):
        r"""Gets the creator of this ComponentList.

        :return: The creator of this ComponentList.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ComponentList.

        :param creator: The creator of this ComponentList.
        :type creator: str
        """
        self._creator = creator

    @property
    def source(self):
        r"""Gets the source of this ComponentList.

        :return: The source of this ComponentList.
        :rtype: :class:`huaweicloudsdkservicestage.v3.SourceObject`
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ComponentList.

        :param source: The source of this ComponentList.
        :type source: :class:`huaweicloudsdkservicestage.v3.SourceObject`
        """
        self._source = source

    @property
    def version(self):
        r"""Gets the version of this ComponentList.

        :return: The version of this ComponentList.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ComponentList.

        :param version: The version of this ComponentList.
        :type version: str
        """
        self._version = version

    @property
    def platform_type(self):
        r"""Gets the platform_type of this ComponentList.

        :return: The platform_type of this ComponentList.
        :rtype: str
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        r"""Sets the platform_type of this ComponentList.

        :param platform_type: The platform_type of this ComponentList.
        :type platform_type: str
        """
        self._platform_type = platform_type

    @property
    def external_accesses(self):
        r"""Gets the external_accesses of this ComponentList.

        :return: The external_accesses of this ComponentList.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.ExternalAccesses`]
        """
        return self._external_accesses

    @external_accesses.setter
    def external_accesses(self, external_accesses):
        r"""Sets the external_accesses of this ComponentList.

        :param external_accesses: The external_accesses of this ComponentList.
        :type external_accesses: list[:class:`huaweicloudsdkservicestage.v3.ExternalAccesses`]
        """
        self._external_accesses = external_accesses

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
        if not isinstance(other, ComponentList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
