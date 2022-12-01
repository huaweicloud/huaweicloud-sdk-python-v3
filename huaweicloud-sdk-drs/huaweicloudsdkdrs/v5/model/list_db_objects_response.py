# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDbObjectsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_root_db': 'TargetRootDb',
        'object_info': 'dict(str, DatabaseObject)',
        'max_table_num': 'int'
    }

    attribute_map = {
        'target_root_db': 'target_root_db',
        'object_info': 'object_info',
        'max_table_num': 'max_table_num'
    }

    def __init__(self, target_root_db=None, object_info=None, max_table_num=None):
        """ListDbObjectsResponse

        The model defined in huaweicloud sdk

        :param target_root_db: 
        :type target_root_db: :class:`huaweicloudsdkdrs.v5.TargetRootDb`
        :param object_info: 数据库对象迁移或同步信息。
        :type object_info: dict(str, DatabaseObject)
        :param max_table_num: 库下表数量的阈值。
        :type max_table_num: int
        """
        
        super(ListDbObjectsResponse, self).__init__()

        self._target_root_db = None
        self._object_info = None
        self._max_table_num = None
        self.discriminator = None

        if target_root_db is not None:
            self.target_root_db = target_root_db
        if object_info is not None:
            self.object_info = object_info
        if max_table_num is not None:
            self.max_table_num = max_table_num

    @property
    def target_root_db(self):
        """Gets the target_root_db of this ListDbObjectsResponse.

        :return: The target_root_db of this ListDbObjectsResponse.
        :rtype: :class:`huaweicloudsdkdrs.v5.TargetRootDb`
        """
        return self._target_root_db

    @target_root_db.setter
    def target_root_db(self, target_root_db):
        """Sets the target_root_db of this ListDbObjectsResponse.

        :param target_root_db: The target_root_db of this ListDbObjectsResponse.
        :type target_root_db: :class:`huaweicloudsdkdrs.v5.TargetRootDb`
        """
        self._target_root_db = target_root_db

    @property
    def object_info(self):
        """Gets the object_info of this ListDbObjectsResponse.

        数据库对象迁移或同步信息。

        :return: The object_info of this ListDbObjectsResponse.
        :rtype: dict(str, DatabaseObject)
        """
        return self._object_info

    @object_info.setter
    def object_info(self, object_info):
        """Sets the object_info of this ListDbObjectsResponse.

        数据库对象迁移或同步信息。

        :param object_info: The object_info of this ListDbObjectsResponse.
        :type object_info: dict(str, DatabaseObject)
        """
        self._object_info = object_info

    @property
    def max_table_num(self):
        """Gets the max_table_num of this ListDbObjectsResponse.

        库下表数量的阈值。

        :return: The max_table_num of this ListDbObjectsResponse.
        :rtype: int
        """
        return self._max_table_num

    @max_table_num.setter
    def max_table_num(self, max_table_num):
        """Sets the max_table_num of this ListDbObjectsResponse.

        库下表数量的阈值。

        :param max_table_num: The max_table_num of this ListDbObjectsResponse.
        :type max_table_num: int
        """
        self._max_table_num = max_table_num

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
        if not isinstance(other, ListDbObjectsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
