# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIpsSwitchStatusUsingGetResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_id': 'str',
        'basic_defense_status': 'int',
        'virtual_patches_stauts': 'int'
    }

    attribute_map = {
        'object_id': 'object_id',
        'basic_defense_status': 'basic_defense_status',
        'virtual_patches_stauts': 'virtual_patches_stauts'
    }

    def __init__(self, object_id=None, basic_defense_status=None, virtual_patches_stauts=None):
        """ListIpsSwitchStatusUsingGetResponse

        The model defined in huaweicloud sdk

        :param object_id: object_id
        :type object_id: str
        :param basic_defense_status: 基础防御状态
        :type basic_defense_status: int
        :param virtual_patches_stauts: 虚拟补丁状态
        :type virtual_patches_stauts: int
        """
        
        super(ListIpsSwitchStatusUsingGetResponse, self).__init__()

        self._object_id = None
        self._basic_defense_status = None
        self._virtual_patches_stauts = None
        self.discriminator = None

        if object_id is not None:
            self.object_id = object_id
        if basic_defense_status is not None:
            self.basic_defense_status = basic_defense_status
        if virtual_patches_stauts is not None:
            self.virtual_patches_stauts = virtual_patches_stauts

    @property
    def object_id(self):
        """Gets the object_id of this ListIpsSwitchStatusUsingGetResponse.

        object_id

        :return: The object_id of this ListIpsSwitchStatusUsingGetResponse.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this ListIpsSwitchStatusUsingGetResponse.

        object_id

        :param object_id: The object_id of this ListIpsSwitchStatusUsingGetResponse.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def basic_defense_status(self):
        """Gets the basic_defense_status of this ListIpsSwitchStatusUsingGetResponse.

        基础防御状态

        :return: The basic_defense_status of this ListIpsSwitchStatusUsingGetResponse.
        :rtype: int
        """
        return self._basic_defense_status

    @basic_defense_status.setter
    def basic_defense_status(self, basic_defense_status):
        """Sets the basic_defense_status of this ListIpsSwitchStatusUsingGetResponse.

        基础防御状态

        :param basic_defense_status: The basic_defense_status of this ListIpsSwitchStatusUsingGetResponse.
        :type basic_defense_status: int
        """
        self._basic_defense_status = basic_defense_status

    @property
    def virtual_patches_stauts(self):
        """Gets the virtual_patches_stauts of this ListIpsSwitchStatusUsingGetResponse.

        虚拟补丁状态

        :return: The virtual_patches_stauts of this ListIpsSwitchStatusUsingGetResponse.
        :rtype: int
        """
        return self._virtual_patches_stauts

    @virtual_patches_stauts.setter
    def virtual_patches_stauts(self, virtual_patches_stauts):
        """Sets the virtual_patches_stauts of this ListIpsSwitchStatusUsingGetResponse.

        虚拟补丁状态

        :param virtual_patches_stauts: The virtual_patches_stauts of this ListIpsSwitchStatusUsingGetResponse.
        :type virtual_patches_stauts: int
        """
        self._virtual_patches_stauts = virtual_patches_stauts

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
        if not isinstance(other, ListIpsSwitchStatusUsingGetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
