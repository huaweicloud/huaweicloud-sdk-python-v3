# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ParameterGroup:

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
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status'
    }

    def __init__(self, id=None, name=None, status=None):
        """ParameterGroup

        The model defined in huaweicloud sdk

        :param id: 参数组ID
        :type id: str
        :param name: 参数组名称
        :type name: str
        :param status: 集群参数状态，有效值包括：  - In-Sync：已同步 - Applying：应用中 - Pending-Reboot：需重启生效 - Sync-Failure：应用失败
        :type status: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status

    @property
    def id(self):
        """Gets the id of this ParameterGroup.

        参数组ID

        :return: The id of this ParameterGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ParameterGroup.

        参数组ID

        :param id: The id of this ParameterGroup.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ParameterGroup.

        参数组名称

        :return: The name of this ParameterGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ParameterGroup.

        参数组名称

        :param name: The name of this ParameterGroup.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ParameterGroup.

        集群参数状态，有效值包括：  - In-Sync：已同步 - Applying：应用中 - Pending-Reboot：需重启生效 - Sync-Failure：应用失败

        :return: The status of this ParameterGroup.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ParameterGroup.

        集群参数状态，有效值包括：  - In-Sync：已同步 - Applying：应用中 - Pending-Reboot：需重启生效 - Sync-Failure：应用失败

        :param status: The status of this ParameterGroup.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ParameterGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
