# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateJobInput:

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
        'description': 'str',
        'type': 'JobType',
        'version': 'JobVersionInput',
        'current_endpoint_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'version': 'version',
        'current_endpoint_id': 'current_endpoint_id'
    }

    def __init__(self, name=None, description=None, type=None, version=None, current_endpoint_id=None):
        r"""CreateJobInput

        The model defined in huaweicloud sdk

        :param name: Job名称,只能包含中文、字母、数字、下划线、中划线、点、空格
        :type name: str
        :param description: 描述信息
        :type description: str
        :param type: 
        :type type: :class:`huaweicloudsdkdataartsfabric.v1.JobType`
        :param version: 
        :type version: :class:`huaweicloudsdkdataartsfabric.v1.JobVersionInput`
        :param current_endpoint_id: Endpoint Id，32~36位的英文、数字、短横组合。
        :type current_endpoint_id: str
        """
        
        

        self._name = None
        self._description = None
        self._type = None
        self._version = None
        self._current_endpoint_id = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.type = type
        self.version = version
        if current_endpoint_id is not None:
            self.current_endpoint_id = current_endpoint_id

    @property
    def name(self):
        r"""Gets the name of this CreateJobInput.

        Job名称,只能包含中文、字母、数字、下划线、中划线、点、空格

        :return: The name of this CreateJobInput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateJobInput.

        Job名称,只能包含中文、字母、数字、下划线、中划线、点、空格

        :param name: The name of this CreateJobInput.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateJobInput.

        描述信息

        :return: The description of this CreateJobInput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateJobInput.

        描述信息

        :param description: The description of this CreateJobInput.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this CreateJobInput.

        :return: The type of this CreateJobInput.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.JobType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateJobInput.

        :param type: The type of this CreateJobInput.
        :type type: :class:`huaweicloudsdkdataartsfabric.v1.JobType`
        """
        self._type = type

    @property
    def version(self):
        r"""Gets the version of this CreateJobInput.

        :return: The version of this CreateJobInput.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.JobVersionInput`
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this CreateJobInput.

        :param version: The version of this CreateJobInput.
        :type version: :class:`huaweicloudsdkdataartsfabric.v1.JobVersionInput`
        """
        self._version = version

    @property
    def current_endpoint_id(self):
        r"""Gets the current_endpoint_id of this CreateJobInput.

        Endpoint Id，32~36位的英文、数字、短横组合。

        :return: The current_endpoint_id of this CreateJobInput.
        :rtype: str
        """
        return self._current_endpoint_id

    @current_endpoint_id.setter
    def current_endpoint_id(self, current_endpoint_id):
        r"""Sets the current_endpoint_id of this CreateJobInput.

        Endpoint Id，32~36位的英文、数字、短横组合。

        :param current_endpoint_id: The current_endpoint_id of this CreateJobInput.
        :type current_endpoint_id: str
        """
        self._current_endpoint_id = current_endpoint_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateJobInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
