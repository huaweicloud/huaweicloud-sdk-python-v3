# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDdmNodeDetailResponse(SdkResponse):

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
        'private_ip': 'str',
        'status': 'str',
        'name': 'str',
        'subnet_id': 'str',
        'az_code': 'str',
        'group_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'private_ip': 'private_ip',
        'status': 'status',
        'name': 'name',
        'subnet_id': 'subnet_id',
        'az_code': 'az_code',
        'group_id': 'group_id'
    }

    def __init__(self, id=None, private_ip=None, status=None, name=None, subnet_id=None, az_code=None, group_id=None):
        r"""ShowDdmNodeDetailResponse

        The model defined in huaweicloud sdk

        :param id: 节点id。
        :type id: str
        :param private_ip: 私有ip。
        :type private_ip: str
        :param status: 节点状态。
        :type status: str
        :param name: 节点名称。
        :type name: str
        :param subnet_id: 子网id。
        :type subnet_id: str
        :param az_code: 可用区。
        :type az_code: str
        :param group_id: 组id。
        :type group_id: str
        """
        
        super().__init__()

        self._id = None
        self._private_ip = None
        self._status = None
        self._name = None
        self._subnet_id = None
        self._az_code = None
        self._group_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if private_ip is not None:
            self.private_ip = private_ip
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if az_code is not None:
            self.az_code = az_code
        if group_id is not None:
            self.group_id = group_id

    @property
    def id(self):
        r"""Gets the id of this ShowDdmNodeDetailResponse.

        节点id。

        :return: The id of this ShowDdmNodeDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowDdmNodeDetailResponse.

        节点id。

        :param id: The id of this ShowDdmNodeDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ShowDdmNodeDetailResponse.

        私有ip。

        :return: The private_ip of this ShowDdmNodeDetailResponse.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ShowDdmNodeDetailResponse.

        私有ip。

        :param private_ip: The private_ip of this ShowDdmNodeDetailResponse.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def status(self):
        r"""Gets the status of this ShowDdmNodeDetailResponse.

        节点状态。

        :return: The status of this ShowDdmNodeDetailResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowDdmNodeDetailResponse.

        节点状态。

        :param status: The status of this ShowDdmNodeDetailResponse.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        r"""Gets the name of this ShowDdmNodeDetailResponse.

        节点名称。

        :return: The name of this ShowDdmNodeDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowDdmNodeDetailResponse.

        节点名称。

        :param name: The name of this ShowDdmNodeDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ShowDdmNodeDetailResponse.

        子网id。

        :return: The subnet_id of this ShowDdmNodeDetailResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ShowDdmNodeDetailResponse.

        子网id。

        :param subnet_id: The subnet_id of this ShowDdmNodeDetailResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def az_code(self):
        r"""Gets the az_code of this ShowDdmNodeDetailResponse.

        可用区。

        :return: The az_code of this ShowDdmNodeDetailResponse.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        r"""Sets the az_code of this ShowDdmNodeDetailResponse.

        可用区。

        :param az_code: The az_code of this ShowDdmNodeDetailResponse.
        :type az_code: str
        """
        self._az_code = az_code

    @property
    def group_id(self):
        r"""Gets the group_id of this ShowDdmNodeDetailResponse.

        组id。

        :return: The group_id of this ShowDdmNodeDetailResponse.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ShowDdmNodeDetailResponse.

        组id。

        :param group_id: The group_id of this ShowDdmNodeDetailResponse.
        :type group_id: str
        """
        self._group_id = group_id

    def to_dict(self):
        import warnings
        warnings.warn("ShowDdmNodeDetailResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowDdmNodeDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
