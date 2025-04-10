# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDbObjectsListResponse(SdkResponse):

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
        'max_table_num': 'int',
        'status': 'str',
        'id': 'str',
        'object_scope': 'str'
    }

    attribute_map = {
        'target_root_db': 'target_root_db',
        'object_info': 'object_info',
        'max_table_num': 'max_table_num',
        'status': 'status',
        'id': 'id',
        'object_scope': 'object_scope'
    }

    def __init__(self, target_root_db=None, object_info=None, max_table_num=None, status=None, id=None, object_scope=None):
        r"""ShowDbObjectsListResponse

        The model defined in huaweicloud sdk

        :param target_root_db: 
        :type target_root_db: :class:`huaweicloudsdkdrs.v5.TargetRootDb`
        :param object_info: 数据库对象迁移或同步信息。
        :type object_info: dict(str, DatabaseObject)
        :param max_table_num: 库下表数量的阈值。
        :type max_table_num: int
        :param status: 获取提交查询对象选择信息的状态
        :type status: str
        :param id: 任务id
        :type id: str
        :param object_scope: 该数据库在实时同步场景下的类型
        :type object_scope: str
        """
        
        super(ShowDbObjectsListResponse, self).__init__()

        self._target_root_db = None
        self._object_info = None
        self._max_table_num = None
        self._status = None
        self._id = None
        self._object_scope = None
        self.discriminator = None

        if target_root_db is not None:
            self.target_root_db = target_root_db
        if object_info is not None:
            self.object_info = object_info
        if max_table_num is not None:
            self.max_table_num = max_table_num
        if status is not None:
            self.status = status
        if id is not None:
            self.id = id
        if object_scope is not None:
            self.object_scope = object_scope

    @property
    def target_root_db(self):
        r"""Gets the target_root_db of this ShowDbObjectsListResponse.

        :return: The target_root_db of this ShowDbObjectsListResponse.
        :rtype: :class:`huaweicloudsdkdrs.v5.TargetRootDb`
        """
        return self._target_root_db

    @target_root_db.setter
    def target_root_db(self, target_root_db):
        r"""Sets the target_root_db of this ShowDbObjectsListResponse.

        :param target_root_db: The target_root_db of this ShowDbObjectsListResponse.
        :type target_root_db: :class:`huaweicloudsdkdrs.v5.TargetRootDb`
        """
        self._target_root_db = target_root_db

    @property
    def object_info(self):
        r"""Gets the object_info of this ShowDbObjectsListResponse.

        数据库对象迁移或同步信息。

        :return: The object_info of this ShowDbObjectsListResponse.
        :rtype: dict(str, DatabaseObject)
        """
        return self._object_info

    @object_info.setter
    def object_info(self, object_info):
        r"""Sets the object_info of this ShowDbObjectsListResponse.

        数据库对象迁移或同步信息。

        :param object_info: The object_info of this ShowDbObjectsListResponse.
        :type object_info: dict(str, DatabaseObject)
        """
        self._object_info = object_info

    @property
    def max_table_num(self):
        r"""Gets the max_table_num of this ShowDbObjectsListResponse.

        库下表数量的阈值。

        :return: The max_table_num of this ShowDbObjectsListResponse.
        :rtype: int
        """
        return self._max_table_num

    @max_table_num.setter
    def max_table_num(self, max_table_num):
        r"""Sets the max_table_num of this ShowDbObjectsListResponse.

        库下表数量的阈值。

        :param max_table_num: The max_table_num of this ShowDbObjectsListResponse.
        :type max_table_num: int
        """
        self._max_table_num = max_table_num

    @property
    def status(self):
        r"""Gets the status of this ShowDbObjectsListResponse.

        获取提交查询对象选择信息的状态

        :return: The status of this ShowDbObjectsListResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowDbObjectsListResponse.

        获取提交查询对象选择信息的状态

        :param status: The status of this ShowDbObjectsListResponse.
        :type status: str
        """
        self._status = status

    @property
    def id(self):
        r"""Gets the id of this ShowDbObjectsListResponse.

        任务id

        :return: The id of this ShowDbObjectsListResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowDbObjectsListResponse.

        任务id

        :param id: The id of this ShowDbObjectsListResponse.
        :type id: str
        """
        self._id = id

    @property
    def object_scope(self):
        r"""Gets the object_scope of this ShowDbObjectsListResponse.

        该数据库在实时同步场景下的类型

        :return: The object_scope of this ShowDbObjectsListResponse.
        :rtype: str
        """
        return self._object_scope

    @object_scope.setter
    def object_scope(self, object_scope):
        r"""Sets the object_scope of this ShowDbObjectsListResponse.

        该数据库在实时同步场景下的类型

        :param object_scope: The object_scope of this ShowDbObjectsListResponse.
        :type object_scope: str
        """
        self._object_scope = object_scope

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
        if not isinstance(other, ShowDbObjectsListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
