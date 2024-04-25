# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataWareHouseDTODwConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fgac_flag': 'bool',
        'fgac_type': 'str',
        'fgac_conn_status': 'str',
        'fgac_conn_test_time': 'int',
        'fgac_conn_test_error': 'str'
    }

    attribute_map = {
        'fgac_flag': 'fgac_flag',
        'fgac_type': 'fgac_type',
        'fgac_conn_status': 'fgac_conn_status',
        'fgac_conn_test_time': 'fgac_conn_test_time',
        'fgac_conn_test_error': 'fgac_conn_test_error'
    }

    def __init__(self, fgac_flag=None, fgac_type=None, fgac_conn_status=None, fgac_conn_test_time=None, fgac_conn_test_error=None):
        """DataWareHouseDTODwConfig

        The model defined in huaweicloud sdk

        :param fgac_flag: 是否开启细粒度认证,true表示开启细粒度认证,false表示关闭细粒度认证。
        :type fgac_flag: bool
        :param fgac_type: 细粒度认证类型，开启细粒度认证时才生效。\&quot;0\&quot;表示开发态细粒度认证，支持数据开发细粒度脚本运行、作业测试运行，\&quot;1\&quot;表示调度态细粒度认证，支持数据开发细粒度脚本运行、作业测试运行、作业执行调度。
        :type fgac_type: str
        :param fgac_conn_status: 数据源连通性测试状态：   * UNKNOWN - 连通性未测试   * TESTING - 连通性测试中   * SUCCESS - 连通性测试成功   * FAILED - 连通性测试失败
        :type fgac_conn_status: str
        :param fgac_conn_test_time: 最近一次连通性测试时间
        :type fgac_conn_test_time: int
        :param fgac_conn_test_error: 联通性测试失败信息，如果连通性测试成功或者未测试联通性，失败信息为空字符串
        :type fgac_conn_test_error: str
        """
        
        

        self._fgac_flag = None
        self._fgac_type = None
        self._fgac_conn_status = None
        self._fgac_conn_test_time = None
        self._fgac_conn_test_error = None
        self.discriminator = None

        if fgac_flag is not None:
            self.fgac_flag = fgac_flag
        if fgac_type is not None:
            self.fgac_type = fgac_type
        if fgac_conn_status is not None:
            self.fgac_conn_status = fgac_conn_status
        if fgac_conn_test_time is not None:
            self.fgac_conn_test_time = fgac_conn_test_time
        if fgac_conn_test_error is not None:
            self.fgac_conn_test_error = fgac_conn_test_error

    @property
    def fgac_flag(self):
        """Gets the fgac_flag of this DataWareHouseDTODwConfig.

        是否开启细粒度认证,true表示开启细粒度认证,false表示关闭细粒度认证。

        :return: The fgac_flag of this DataWareHouseDTODwConfig.
        :rtype: bool
        """
        return self._fgac_flag

    @fgac_flag.setter
    def fgac_flag(self, fgac_flag):
        """Sets the fgac_flag of this DataWareHouseDTODwConfig.

        是否开启细粒度认证,true表示开启细粒度认证,false表示关闭细粒度认证。

        :param fgac_flag: The fgac_flag of this DataWareHouseDTODwConfig.
        :type fgac_flag: bool
        """
        self._fgac_flag = fgac_flag

    @property
    def fgac_type(self):
        """Gets the fgac_type of this DataWareHouseDTODwConfig.

        细粒度认证类型，开启细粒度认证时才生效。\"0\"表示开发态细粒度认证，支持数据开发细粒度脚本运行、作业测试运行，\"1\"表示调度态细粒度认证，支持数据开发细粒度脚本运行、作业测试运行、作业执行调度。

        :return: The fgac_type of this DataWareHouseDTODwConfig.
        :rtype: str
        """
        return self._fgac_type

    @fgac_type.setter
    def fgac_type(self, fgac_type):
        """Sets the fgac_type of this DataWareHouseDTODwConfig.

        细粒度认证类型，开启细粒度认证时才生效。\"0\"表示开发态细粒度认证，支持数据开发细粒度脚本运行、作业测试运行，\"1\"表示调度态细粒度认证，支持数据开发细粒度脚本运行、作业测试运行、作业执行调度。

        :param fgac_type: The fgac_type of this DataWareHouseDTODwConfig.
        :type fgac_type: str
        """
        self._fgac_type = fgac_type

    @property
    def fgac_conn_status(self):
        """Gets the fgac_conn_status of this DataWareHouseDTODwConfig.

        数据源连通性测试状态：   * UNKNOWN - 连通性未测试   * TESTING - 连通性测试中   * SUCCESS - 连通性测试成功   * FAILED - 连通性测试失败

        :return: The fgac_conn_status of this DataWareHouseDTODwConfig.
        :rtype: str
        """
        return self._fgac_conn_status

    @fgac_conn_status.setter
    def fgac_conn_status(self, fgac_conn_status):
        """Sets the fgac_conn_status of this DataWareHouseDTODwConfig.

        数据源连通性测试状态：   * UNKNOWN - 连通性未测试   * TESTING - 连通性测试中   * SUCCESS - 连通性测试成功   * FAILED - 连通性测试失败

        :param fgac_conn_status: The fgac_conn_status of this DataWareHouseDTODwConfig.
        :type fgac_conn_status: str
        """
        self._fgac_conn_status = fgac_conn_status

    @property
    def fgac_conn_test_time(self):
        """Gets the fgac_conn_test_time of this DataWareHouseDTODwConfig.

        最近一次连通性测试时间

        :return: The fgac_conn_test_time of this DataWareHouseDTODwConfig.
        :rtype: int
        """
        return self._fgac_conn_test_time

    @fgac_conn_test_time.setter
    def fgac_conn_test_time(self, fgac_conn_test_time):
        """Sets the fgac_conn_test_time of this DataWareHouseDTODwConfig.

        最近一次连通性测试时间

        :param fgac_conn_test_time: The fgac_conn_test_time of this DataWareHouseDTODwConfig.
        :type fgac_conn_test_time: int
        """
        self._fgac_conn_test_time = fgac_conn_test_time

    @property
    def fgac_conn_test_error(self):
        """Gets the fgac_conn_test_error of this DataWareHouseDTODwConfig.

        联通性测试失败信息，如果连通性测试成功或者未测试联通性，失败信息为空字符串

        :return: The fgac_conn_test_error of this DataWareHouseDTODwConfig.
        :rtype: str
        """
        return self._fgac_conn_test_error

    @fgac_conn_test_error.setter
    def fgac_conn_test_error(self, fgac_conn_test_error):
        """Sets the fgac_conn_test_error of this DataWareHouseDTODwConfig.

        联通性测试失败信息，如果连通性测试成功或者未测试联通性，失败信息为空字符串

        :param fgac_conn_test_error: The fgac_conn_test_error of this DataWareHouseDTODwConfig.
        :type fgac_conn_test_error: str
        """
        self._fgac_conn_test_error = fgac_conn_test_error

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
        if not isinstance(other, DataWareHouseDTODwConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
