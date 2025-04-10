# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAvailableNodeTypesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'engine_type': 'str',
        'db_use_type': 'str',
        'job_direction': 'str',
        'is_use_sellout_info': 'bool',
        'is_multi_write': 'bool'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'engine_type': 'engine_type',
        'db_use_type': 'db_use_type',
        'job_direction': 'job_direction',
        'is_use_sellout_info': 'is_use_sellout_info',
        'is_multi_write': 'is_multi_write'
    }

    def __init__(self, x_language=None, engine_type=None, db_use_type=None, job_direction=None, is_use_sellout_info=None, is_multi_write=None):
        r"""ListAvailableNodeTypesRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。
        :type x_language: str
        :param engine_type: 引擎类型
        :type engine_type: str
        :param db_use_type: 迁移场景。 - migration:实时迁移 - sync:实时同步 - cloudDataGuard:实时灾备
        :type db_use_type: str
        :param job_direction: 迁移方向，up：入云 ，down：出云，non-dbs：自建。
        :type job_direction: str
        :param is_use_sellout_info: 是否查询资源售罄情况
        :type is_use_sellout_info: bool
        :param is_multi_write: 是否是双主灾备
        :type is_multi_write: bool
        """
        
        

        self._x_language = None
        self._engine_type = None
        self._db_use_type = None
        self._job_direction = None
        self._is_use_sellout_info = None
        self._is_multi_write = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.engine_type = engine_type
        self.db_use_type = db_use_type
        self.job_direction = job_direction
        if is_use_sellout_info is not None:
            self.is_use_sellout_info = is_use_sellout_info
        if is_multi_write is not None:
            self.is_multi_write = is_multi_write

    @property
    def x_language(self):
        r"""Gets the x_language of this ListAvailableNodeTypesRequest.

        请求语言类型。

        :return: The x_language of this ListAvailableNodeTypesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListAvailableNodeTypesRequest.

        请求语言类型。

        :param x_language: The x_language of this ListAvailableNodeTypesRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ListAvailableNodeTypesRequest.

        引擎类型

        :return: The engine_type of this ListAvailableNodeTypesRequest.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ListAvailableNodeTypesRequest.

        引擎类型

        :param engine_type: The engine_type of this ListAvailableNodeTypesRequest.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def db_use_type(self):
        r"""Gets the db_use_type of this ListAvailableNodeTypesRequest.

        迁移场景。 - migration:实时迁移 - sync:实时同步 - cloudDataGuard:实时灾备

        :return: The db_use_type of this ListAvailableNodeTypesRequest.
        :rtype: str
        """
        return self._db_use_type

    @db_use_type.setter
    def db_use_type(self, db_use_type):
        r"""Sets the db_use_type of this ListAvailableNodeTypesRequest.

        迁移场景。 - migration:实时迁移 - sync:实时同步 - cloudDataGuard:实时灾备

        :param db_use_type: The db_use_type of this ListAvailableNodeTypesRequest.
        :type db_use_type: str
        """
        self._db_use_type = db_use_type

    @property
    def job_direction(self):
        r"""Gets the job_direction of this ListAvailableNodeTypesRequest.

        迁移方向，up：入云 ，down：出云，non-dbs：自建。

        :return: The job_direction of this ListAvailableNodeTypesRequest.
        :rtype: str
        """
        return self._job_direction

    @job_direction.setter
    def job_direction(self, job_direction):
        r"""Sets the job_direction of this ListAvailableNodeTypesRequest.

        迁移方向，up：入云 ，down：出云，non-dbs：自建。

        :param job_direction: The job_direction of this ListAvailableNodeTypesRequest.
        :type job_direction: str
        """
        self._job_direction = job_direction

    @property
    def is_use_sellout_info(self):
        r"""Gets the is_use_sellout_info of this ListAvailableNodeTypesRequest.

        是否查询资源售罄情况

        :return: The is_use_sellout_info of this ListAvailableNodeTypesRequest.
        :rtype: bool
        """
        return self._is_use_sellout_info

    @is_use_sellout_info.setter
    def is_use_sellout_info(self, is_use_sellout_info):
        r"""Sets the is_use_sellout_info of this ListAvailableNodeTypesRequest.

        是否查询资源售罄情况

        :param is_use_sellout_info: The is_use_sellout_info of this ListAvailableNodeTypesRequest.
        :type is_use_sellout_info: bool
        """
        self._is_use_sellout_info = is_use_sellout_info

    @property
    def is_multi_write(self):
        r"""Gets the is_multi_write of this ListAvailableNodeTypesRequest.

        是否是双主灾备

        :return: The is_multi_write of this ListAvailableNodeTypesRequest.
        :rtype: bool
        """
        return self._is_multi_write

    @is_multi_write.setter
    def is_multi_write(self, is_multi_write):
        r"""Sets the is_multi_write of this ListAvailableNodeTypesRequest.

        是否是双主灾备

        :param is_multi_write: The is_multi_write of this ListAvailableNodeTypesRequest.
        :type is_multi_write: bool
        """
        self._is_multi_write = is_multi_write

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
        if not isinstance(other, ListAvailableNodeTypesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
