# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ColumnProcessObjects:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_source_names': 'list[str]',
        'object_alias_name': 'str',
        'is_sent': 'bool',
        'extra_column_infos': 'list[AddColumnInfo]'
    }

    attribute_map = {
        'object_source_names': 'object_source_names',
        'object_alias_name': 'object_alias_name',
        'is_sent': 'is_sent',
        'extra_column_infos': 'extra_column_infos'
    }

    def __init__(self, object_source_names=None, object_alias_name=None, is_sent=None, extra_column_infos=None):
        r"""ColumnProcessObjects

        The model defined in huaweicloud sdk

        :param object_source_names: 选择的源库对象名
        :type object_source_names: list[str]
        :param object_alias_name: 映射后的对象名
        :type object_alias_name: str
        :param is_sent: 附加列是否已下发
        :type is_sent: bool
        :param extra_column_infos: 附加列信息
        :type extra_column_infos: list[:class:`huaweicloudsdkdrs.v5.AddColumnInfo`]
        """
        
        

        self._object_source_names = None
        self._object_alias_name = None
        self._is_sent = None
        self._extra_column_infos = None
        self.discriminator = None

        if object_source_names is not None:
            self.object_source_names = object_source_names
        if object_alias_name is not None:
            self.object_alias_name = object_alias_name
        if is_sent is not None:
            self.is_sent = is_sent
        if extra_column_infos is not None:
            self.extra_column_infos = extra_column_infos

    @property
    def object_source_names(self):
        r"""Gets the object_source_names of this ColumnProcessObjects.

        选择的源库对象名

        :return: The object_source_names of this ColumnProcessObjects.
        :rtype: list[str]
        """
        return self._object_source_names

    @object_source_names.setter
    def object_source_names(self, object_source_names):
        r"""Sets the object_source_names of this ColumnProcessObjects.

        选择的源库对象名

        :param object_source_names: The object_source_names of this ColumnProcessObjects.
        :type object_source_names: list[str]
        """
        self._object_source_names = object_source_names

    @property
    def object_alias_name(self):
        r"""Gets the object_alias_name of this ColumnProcessObjects.

        映射后的对象名

        :return: The object_alias_name of this ColumnProcessObjects.
        :rtype: str
        """
        return self._object_alias_name

    @object_alias_name.setter
    def object_alias_name(self, object_alias_name):
        r"""Sets the object_alias_name of this ColumnProcessObjects.

        映射后的对象名

        :param object_alias_name: The object_alias_name of this ColumnProcessObjects.
        :type object_alias_name: str
        """
        self._object_alias_name = object_alias_name

    @property
    def is_sent(self):
        r"""Gets the is_sent of this ColumnProcessObjects.

        附加列是否已下发

        :return: The is_sent of this ColumnProcessObjects.
        :rtype: bool
        """
        return self._is_sent

    @is_sent.setter
    def is_sent(self, is_sent):
        r"""Sets the is_sent of this ColumnProcessObjects.

        附加列是否已下发

        :param is_sent: The is_sent of this ColumnProcessObjects.
        :type is_sent: bool
        """
        self._is_sent = is_sent

    @property
    def extra_column_infos(self):
        r"""Gets the extra_column_infos of this ColumnProcessObjects.

        附加列信息

        :return: The extra_column_infos of this ColumnProcessObjects.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.AddColumnInfo`]
        """
        return self._extra_column_infos

    @extra_column_infos.setter
    def extra_column_infos(self, extra_column_infos):
        r"""Sets the extra_column_infos of this ColumnProcessObjects.

        附加列信息

        :param extra_column_infos: The extra_column_infos of this ColumnProcessObjects.
        :type extra_column_infos: list[:class:`huaweicloudsdkdrs.v5.AddColumnInfo`]
        """
        self._extra_column_infos = extra_column_infos

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
        if not isinstance(other, ColumnProcessObjects):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
