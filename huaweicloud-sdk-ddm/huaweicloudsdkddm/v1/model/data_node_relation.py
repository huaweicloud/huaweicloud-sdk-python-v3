# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataNodeRelation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_instance_id': 'str',
        'target_instance_id': 'str'
    }

    attribute_map = {
        'source_instance_id': 'source_instance_id',
        'target_instance_id': 'target_instance_id'
    }

    def __init__(self, source_instance_id=None, target_instance_id=None):
        r"""DataNodeRelation

        The model defined in huaweicloud sdk

        :param source_instance_id: 源实例id。
        :type source_instance_id: str
        :param target_instance_id: 目标实例id。
        :type target_instance_id: str
        """
        
        

        self._source_instance_id = None
        self._target_instance_id = None
        self.discriminator = None

        if source_instance_id is not None:
            self.source_instance_id = source_instance_id
        if target_instance_id is not None:
            self.target_instance_id = target_instance_id

    @property
    def source_instance_id(self):
        r"""Gets the source_instance_id of this DataNodeRelation.

        源实例id。

        :return: The source_instance_id of this DataNodeRelation.
        :rtype: str
        """
        return self._source_instance_id

    @source_instance_id.setter
    def source_instance_id(self, source_instance_id):
        r"""Sets the source_instance_id of this DataNodeRelation.

        源实例id。

        :param source_instance_id: The source_instance_id of this DataNodeRelation.
        :type source_instance_id: str
        """
        self._source_instance_id = source_instance_id

    @property
    def target_instance_id(self):
        r"""Gets the target_instance_id of this DataNodeRelation.

        目标实例id。

        :return: The target_instance_id of this DataNodeRelation.
        :rtype: str
        """
        return self._target_instance_id

    @target_instance_id.setter
    def target_instance_id(self, target_instance_id):
        r"""Sets the target_instance_id of this DataNodeRelation.

        目标实例id。

        :param target_instance_id: The target_instance_id of this DataNodeRelation.
        :type target_instance_id: str
        """
        self._target_instance_id = target_instance_id

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
        if not isinstance(other, DataNodeRelation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
