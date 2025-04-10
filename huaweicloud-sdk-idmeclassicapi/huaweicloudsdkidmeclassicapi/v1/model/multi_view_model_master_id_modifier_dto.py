# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MultiViewModelMasterIdModifierDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'master_id': 'str',
        'modifier': 'str',
        'item': 'ObjectReferenceParamDTO'
    }

    attribute_map = {
        'master_id': 'masterId',
        'modifier': 'modifier',
        'item': 'item'
    }

    def __init__(self, master_id=None, modifier=None, item=None):
        r"""MultiViewModelMasterIdModifierDTO

        The model defined in huaweicloud sdk

        :param master_id: 主对象ID。
        :type master_id: str
        :param modifier: 处理人。
        :type modifier: str
        :param item: 
        :type item: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        
        

        self._master_id = None
        self._modifier = None
        self._item = None
        self.discriminator = None

        self.master_id = master_id
        if modifier is not None:
            self.modifier = modifier
        if item is not None:
            self.item = item

    @property
    def master_id(self):
        r"""Gets the master_id of this MultiViewModelMasterIdModifierDTO.

        主对象ID。

        :return: The master_id of this MultiViewModelMasterIdModifierDTO.
        :rtype: str
        """
        return self._master_id

    @master_id.setter
    def master_id(self, master_id):
        r"""Sets the master_id of this MultiViewModelMasterIdModifierDTO.

        主对象ID。

        :param master_id: The master_id of this MultiViewModelMasterIdModifierDTO.
        :type master_id: str
        """
        self._master_id = master_id

    @property
    def modifier(self):
        r"""Gets the modifier of this MultiViewModelMasterIdModifierDTO.

        处理人。

        :return: The modifier of this MultiViewModelMasterIdModifierDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        r"""Sets the modifier of this MultiViewModelMasterIdModifierDTO.

        处理人。

        :param modifier: The modifier of this MultiViewModelMasterIdModifierDTO.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def item(self):
        r"""Gets the item of this MultiViewModelMasterIdModifierDTO.

        :return: The item of this MultiViewModelMasterIdModifierDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        return self._item

    @item.setter
    def item(self, item):
        r"""Sets the item of this MultiViewModelMasterIdModifierDTO.

        :param item: The item of this MultiViewModelMasterIdModifierDTO.
        :type item: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        self._item = item

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
        if not isinstance(other, MultiViewModelMasterIdModifierDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
