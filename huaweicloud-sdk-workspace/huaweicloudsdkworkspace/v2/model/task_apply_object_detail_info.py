# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskApplyObjectDetailInfo:

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
        'object_type': 'str',
        'object_name': 'str',
        'object_extra_id': 'str'
    }

    attribute_map = {
        'object_id': 'object_id',
        'object_type': 'object_type',
        'object_name': 'object_name',
        'object_extra_id': 'object_extra_id'
    }

    def __init__(self, object_id=None, object_type=None, object_name=None, object_extra_id=None):
        r"""TaskApplyObjectDetailInfo

        The model defined in huaweicloud sdk

        :param object_id: 对象id
        :type object_id: str
        :param object_type: 对象类型
        :type object_type: str
        :param object_name: 对象名称
        :type object_name: str
        :param object_extra_id: 对象desktopId
        :type object_extra_id: str
        """
        
        

        self._object_id = None
        self._object_type = None
        self._object_name = None
        self._object_extra_id = None
        self.discriminator = None

        if object_id is not None:
            self.object_id = object_id
        if object_type is not None:
            self.object_type = object_type
        if object_name is not None:
            self.object_name = object_name
        if object_extra_id is not None:
            self.object_extra_id = object_extra_id

    @property
    def object_id(self):
        r"""Gets the object_id of this TaskApplyObjectDetailInfo.

        对象id

        :return: The object_id of this TaskApplyObjectDetailInfo.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this TaskApplyObjectDetailInfo.

        对象id

        :param object_id: The object_id of this TaskApplyObjectDetailInfo.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def object_type(self):
        r"""Gets the object_type of this TaskApplyObjectDetailInfo.

        对象类型

        :return: The object_type of this TaskApplyObjectDetailInfo.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        r"""Sets the object_type of this TaskApplyObjectDetailInfo.

        对象类型

        :param object_type: The object_type of this TaskApplyObjectDetailInfo.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def object_name(self):
        r"""Gets the object_name of this TaskApplyObjectDetailInfo.

        对象名称

        :return: The object_name of this TaskApplyObjectDetailInfo.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        r"""Sets the object_name of this TaskApplyObjectDetailInfo.

        对象名称

        :param object_name: The object_name of this TaskApplyObjectDetailInfo.
        :type object_name: str
        """
        self._object_name = object_name

    @property
    def object_extra_id(self):
        r"""Gets the object_extra_id of this TaskApplyObjectDetailInfo.

        对象desktopId

        :return: The object_extra_id of this TaskApplyObjectDetailInfo.
        :rtype: str
        """
        return self._object_extra_id

    @object_extra_id.setter
    def object_extra_id(self, object_extra_id):
        r"""Sets the object_extra_id of this TaskApplyObjectDetailInfo.

        对象desktopId

        :param object_extra_id: The object_extra_id of this TaskApplyObjectDetailInfo.
        :type object_extra_id: str
        """
        self._object_extra_id = object_extra_id

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
        if not isinstance(other, TaskApplyObjectDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
