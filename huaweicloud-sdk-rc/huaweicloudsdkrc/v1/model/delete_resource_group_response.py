# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteResourceGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'domain_id': 'str',
        'group_name': 'str',
        'description': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'domain_id': 'domain_id',
        'group_name': 'group_name',
        'description': 'description',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, group_id=None, domain_id=None, group_name=None, description=None, create_time=None, update_time=None):
        r"""DeleteResourceGroupResponse

        The model defined in huaweicloud sdk

        :param group_id: uuid
        :type group_id: str
        :param domain_id: 
        :type domain_id: str
        :param group_name: 
        :type group_name: str
        :param description: 
        :type description: str
        :param create_time: 
        :type create_time: str
        :param update_time: 
        :type update_time: str
        """
        
        super().__init__()

        self._group_id = None
        self._domain_id = None
        self._group_name = None
        self._description = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if domain_id is not None:
            self.domain_id = domain_id
        if group_name is not None:
            self.group_name = group_name
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def group_id(self):
        r"""Gets the group_id of this DeleteResourceGroupResponse.

        uuid

        :return: The group_id of this DeleteResourceGroupResponse.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this DeleteResourceGroupResponse.

        uuid

        :param group_id: The group_id of this DeleteResourceGroupResponse.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this DeleteResourceGroupResponse.

        :return: The domain_id of this DeleteResourceGroupResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this DeleteResourceGroupResponse.

        :param domain_id: The domain_id of this DeleteResourceGroupResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def group_name(self):
        r"""Gets the group_name of this DeleteResourceGroupResponse.

        :return: The group_name of this DeleteResourceGroupResponse.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this DeleteResourceGroupResponse.

        :param group_name: The group_name of this DeleteResourceGroupResponse.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def description(self):
        r"""Gets the description of this DeleteResourceGroupResponse.

        :return: The description of this DeleteResourceGroupResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DeleteResourceGroupResponse.

        :param description: The description of this DeleteResourceGroupResponse.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this DeleteResourceGroupResponse.

        :return: The create_time of this DeleteResourceGroupResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this DeleteResourceGroupResponse.

        :param create_time: The create_time of this DeleteResourceGroupResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this DeleteResourceGroupResponse.

        :return: The update_time of this DeleteResourceGroupResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this DeleteResourceGroupResponse.

        :param update_time: The update_time of this DeleteResourceGroupResponse.
        :type update_time: str
        """
        self._update_time = update_time

    def to_dict(self):
        import warnings
        warnings.warn("DeleteResourceGroupResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, DeleteResourceGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
