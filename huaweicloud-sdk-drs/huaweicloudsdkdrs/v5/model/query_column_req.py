# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryColumnReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_force_refresh': 'bool',
        'db_object_infos': 'list[SelectDbTableObjectInfo]'
    }

    attribute_map = {
        'is_force_refresh': 'is_force_refresh',
        'db_object_infos': 'db_object_infos'
    }

    def __init__(self, is_force_refresh=None, db_object_infos=None):
        """QueryColumnReq

        The model defined in huaweicloud sdk

        :param is_force_refresh: 是否从Node获取最新的列信息
        :type is_force_refresh: bool
        :param db_object_infos: 指定数据库表信息
        :type db_object_infos: list[:class:`huaweicloudsdkdrs.v5.SelectDbTableObjectInfo`]
        """
        
        

        self._is_force_refresh = None
        self._db_object_infos = None
        self.discriminator = None

        if is_force_refresh is not None:
            self.is_force_refresh = is_force_refresh
        self.db_object_infos = db_object_infos

    @property
    def is_force_refresh(self):
        """Gets the is_force_refresh of this QueryColumnReq.

        是否从Node获取最新的列信息

        :return: The is_force_refresh of this QueryColumnReq.
        :rtype: bool
        """
        return self._is_force_refresh

    @is_force_refresh.setter
    def is_force_refresh(self, is_force_refresh):
        """Sets the is_force_refresh of this QueryColumnReq.

        是否从Node获取最新的列信息

        :param is_force_refresh: The is_force_refresh of this QueryColumnReq.
        :type is_force_refresh: bool
        """
        self._is_force_refresh = is_force_refresh

    @property
    def db_object_infos(self):
        """Gets the db_object_infos of this QueryColumnReq.

        指定数据库表信息

        :return: The db_object_infos of this QueryColumnReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.SelectDbTableObjectInfo`]
        """
        return self._db_object_infos

    @db_object_infos.setter
    def db_object_infos(self, db_object_infos):
        """Sets the db_object_infos of this QueryColumnReq.

        指定数据库表信息

        :param db_object_infos: The db_object_infos of this QueryColumnReq.
        :type db_object_infos: list[:class:`huaweicloudsdkdrs.v5.SelectDbTableObjectInfo`]
        """
        self._db_object_infos = db_object_infos

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
        if not isinstance(other, QueryColumnReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
