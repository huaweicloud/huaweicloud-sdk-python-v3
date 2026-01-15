# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowColumnInfoReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'refresh': 'bool',
        'object_ids': 'list[str]'
    }

    attribute_map = {
        'refresh': 'refresh',
        'object_ids': 'object_ids'
    }

    def __init__(self, refresh=None, object_ids=None):
        r"""ShowColumnInfoReq

        The model defined in huaweicloud sdk

        :param refresh: 是否重新从node获取列信息
        :type refresh: bool
        :param object_ids: 列所属的对象信息
        :type object_ids: list[str]
        """
        
        

        self._refresh = None
        self._object_ids = None
        self.discriminator = None

        self.refresh = refresh
        if object_ids is not None:
            self.object_ids = object_ids

    @property
    def refresh(self):
        r"""Gets the refresh of this ShowColumnInfoReq.

        是否重新从node获取列信息

        :return: The refresh of this ShowColumnInfoReq.
        :rtype: bool
        """
        return self._refresh

    @refresh.setter
    def refresh(self, refresh):
        r"""Sets the refresh of this ShowColumnInfoReq.

        是否重新从node获取列信息

        :param refresh: The refresh of this ShowColumnInfoReq.
        :type refresh: bool
        """
        self._refresh = refresh

    @property
    def object_ids(self):
        r"""Gets the object_ids of this ShowColumnInfoReq.

        列所属的对象信息

        :return: The object_ids of this ShowColumnInfoReq.
        :rtype: list[str]
        """
        return self._object_ids

    @object_ids.setter
    def object_ids(self, object_ids):
        r"""Sets the object_ids of this ShowColumnInfoReq.

        列所属的对象信息

        :param object_ids: The object_ids of this ShowColumnInfoReq.
        :type object_ids: list[str]
        """
        self._object_ids = object_ids

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
        if not isinstance(other, ShowColumnInfoReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
