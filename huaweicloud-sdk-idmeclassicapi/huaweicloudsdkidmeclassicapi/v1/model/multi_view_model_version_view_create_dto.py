# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MultiViewModelVersionViewCreateDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'modifier': 'str',
        'version_id': 'str',
        'work_copy_type': 'str',
        'custom_link_set': 'list[str]',
        'need_set_null': 'list[str]',
        'item': 'ObjectReferenceParamDTO'
    }

    attribute_map = {
        'modifier': 'modifier',
        'version_id': 'versionId',
        'work_copy_type': 'workCopyType',
        'custom_link_set': 'customLinkSet',
        'need_set_null': 'needSetNull',
        'item': 'item'
    }

    def __init__(self, modifier=None, version_id=None, work_copy_type=None, custom_link_set=None, need_set_null=None, item=None):
        """MultiViewModelVersionViewCreateDTO

        The model defined in huaweicloud sdk

        :param modifier: 修改人。
        :type modifier: str
        :param version_id: 版本对象ID。
        :type version_id: str
        :param work_copy_type: 关系的复制类型。 - BOTH：复制当前M-V模型作为源端与目标端的关系。 - CUSTOM：自定义复制当前M-V模型的关系。 - NONE：不复制当前M-V模型的关系。 - SOURCE：仅复制当前M-V模型作为源端的关系。 - TARGET：仅复制当前M-V模型作为目标端的关系。
        :type work_copy_type: str
        :param custom_link_set: 关系实体名称集合，与workCopyType的值CUSTOM配合使用。
        :type custom_link_set: list[str]
        :param need_set_null: 指定不复制的属性，其值将被设置为null。
        :type need_set_null: list[str]
        :param item: 
        :type item: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        
        

        self._modifier = None
        self._version_id = None
        self._work_copy_type = None
        self._custom_link_set = None
        self._need_set_null = None
        self._item = None
        self.discriminator = None

        if modifier is not None:
            self.modifier = modifier
        self.version_id = version_id
        if work_copy_type is not None:
            self.work_copy_type = work_copy_type
        if custom_link_set is not None:
            self.custom_link_set = custom_link_set
        if need_set_null is not None:
            self.need_set_null = need_set_null
        self.item = item

    @property
    def modifier(self):
        """Gets the modifier of this MultiViewModelVersionViewCreateDTO.

        修改人。

        :return: The modifier of this MultiViewModelVersionViewCreateDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        """Sets the modifier of this MultiViewModelVersionViewCreateDTO.

        修改人。

        :param modifier: The modifier of this MultiViewModelVersionViewCreateDTO.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def version_id(self):
        """Gets the version_id of this MultiViewModelVersionViewCreateDTO.

        版本对象ID。

        :return: The version_id of this MultiViewModelVersionViewCreateDTO.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this MultiViewModelVersionViewCreateDTO.

        版本对象ID。

        :param version_id: The version_id of this MultiViewModelVersionViewCreateDTO.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def work_copy_type(self):
        """Gets the work_copy_type of this MultiViewModelVersionViewCreateDTO.

        关系的复制类型。 - BOTH：复制当前M-V模型作为源端与目标端的关系。 - CUSTOM：自定义复制当前M-V模型的关系。 - NONE：不复制当前M-V模型的关系。 - SOURCE：仅复制当前M-V模型作为源端的关系。 - TARGET：仅复制当前M-V模型作为目标端的关系。

        :return: The work_copy_type of this MultiViewModelVersionViewCreateDTO.
        :rtype: str
        """
        return self._work_copy_type

    @work_copy_type.setter
    def work_copy_type(self, work_copy_type):
        """Sets the work_copy_type of this MultiViewModelVersionViewCreateDTO.

        关系的复制类型。 - BOTH：复制当前M-V模型作为源端与目标端的关系。 - CUSTOM：自定义复制当前M-V模型的关系。 - NONE：不复制当前M-V模型的关系。 - SOURCE：仅复制当前M-V模型作为源端的关系。 - TARGET：仅复制当前M-V模型作为目标端的关系。

        :param work_copy_type: The work_copy_type of this MultiViewModelVersionViewCreateDTO.
        :type work_copy_type: str
        """
        self._work_copy_type = work_copy_type

    @property
    def custom_link_set(self):
        """Gets the custom_link_set of this MultiViewModelVersionViewCreateDTO.

        关系实体名称集合，与workCopyType的值CUSTOM配合使用。

        :return: The custom_link_set of this MultiViewModelVersionViewCreateDTO.
        :rtype: list[str]
        """
        return self._custom_link_set

    @custom_link_set.setter
    def custom_link_set(self, custom_link_set):
        """Sets the custom_link_set of this MultiViewModelVersionViewCreateDTO.

        关系实体名称集合，与workCopyType的值CUSTOM配合使用。

        :param custom_link_set: The custom_link_set of this MultiViewModelVersionViewCreateDTO.
        :type custom_link_set: list[str]
        """
        self._custom_link_set = custom_link_set

    @property
    def need_set_null(self):
        """Gets the need_set_null of this MultiViewModelVersionViewCreateDTO.

        指定不复制的属性，其值将被设置为null。

        :return: The need_set_null of this MultiViewModelVersionViewCreateDTO.
        :rtype: list[str]
        """
        return self._need_set_null

    @need_set_null.setter
    def need_set_null(self, need_set_null):
        """Sets the need_set_null of this MultiViewModelVersionViewCreateDTO.

        指定不复制的属性，其值将被设置为null。

        :param need_set_null: The need_set_null of this MultiViewModelVersionViewCreateDTO.
        :type need_set_null: list[str]
        """
        self._need_set_null = need_set_null

    @property
    def item(self):
        """Gets the item of this MultiViewModelVersionViewCreateDTO.

        :return: The item of this MultiViewModelVersionViewCreateDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this MultiViewModelVersionViewCreateDTO.

        :param item: The item of this MultiViewModelVersionViewCreateDTO.
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
        if not isinstance(other, MultiViewModelVersionViewCreateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
