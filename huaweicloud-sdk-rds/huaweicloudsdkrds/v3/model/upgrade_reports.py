# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeReports:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'src_instance_id': 'str',
        'src_database_version': 'str',
        'dst_instance_id': 'str',
        'dst_database_version': 'str',
        'result': 'str',
        'is_private_ip_changed': 'bool',
        'private_ip_change_time': 'str',
        'statistics_collection_mode': 'str',
        'detail': 'str'
    }

    attribute_map = {
        'id': 'id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'src_instance_id': 'src_instance_id',
        'src_database_version': 'src_database_version',
        'dst_instance_id': 'dst_instance_id',
        'dst_database_version': 'dst_database_version',
        'result': 'result',
        'is_private_ip_changed': 'is_private_ip_changed',
        'private_ip_change_time': 'private_ip_change_time',
        'statistics_collection_mode': 'statistics_collection_mode',
        'detail': 'detail'
    }

    def __init__(self, id=None, start_time=None, end_time=None, src_instance_id=None, src_database_version=None, dst_instance_id=None, dst_database_version=None, result=None, is_private_ip_changed=None, private_ip_change_time=None, statistics_collection_mode=None, detail=None):
        r"""UpgradeReports

        The model defined in huaweicloud sdk

        :param id: 升级报告ID。
        :type id: str
        :param start_time: 升级开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type start_time: str
        :param end_time: 升级结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type end_time: str
        :param src_instance_id: 原实例ID。
        :type src_instance_id: str
        :param src_database_version: 原数据库版本。
        :type src_database_version: str
        :param dst_instance_id: 目标实例ID。
        :type dst_instance_id: str
        :param dst_database_version: 目标数据库版本。
        :type dst_database_version: str
        :param result: 升级结果。 success，表示成功。 failed，表示失败。 running， 表示升级中。
        :type result: str
        :param is_private_ip_changed: 实例内网IP是否改变。 true，表示改变。 false，表示不改变。
        :type is_private_ip_changed: bool
        :param private_ip_change_time: 实例内网IP修改时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type private_ip_change_time: str
        :param statistics_collection_mode: 统计信息收集模式。 before_change_private_ip，修改实例内网IP前收集。 after_change_private_ip，修改实例内网IP后收集。
        :type statistics_collection_mode: str
        :param detail: 升级报告详情。
        :type detail: str
        """
        
        

        self._id = None
        self._start_time = None
        self._end_time = None
        self._src_instance_id = None
        self._src_database_version = None
        self._dst_instance_id = None
        self._dst_database_version = None
        self._result = None
        self._is_private_ip_changed = None
        self._private_ip_change_time = None
        self._statistics_collection_mode = None
        self._detail = None
        self.discriminator = None

        self.id = id
        self.start_time = start_time
        self.end_time = end_time
        self.src_instance_id = src_instance_id
        self.src_database_version = src_database_version
        self.dst_instance_id = dst_instance_id
        self.dst_database_version = dst_database_version
        self.result = result
        self.is_private_ip_changed = is_private_ip_changed
        self.private_ip_change_time = private_ip_change_time
        self.statistics_collection_mode = statistics_collection_mode
        self.detail = detail

    @property
    def id(self):
        r"""Gets the id of this UpgradeReports.

        升级报告ID。

        :return: The id of this UpgradeReports.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpgradeReports.

        升级报告ID。

        :param id: The id of this UpgradeReports.
        :type id: str
        """
        self._id = id

    @property
    def start_time(self):
        r"""Gets the start_time of this UpgradeReports.

        升级开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The start_time of this UpgradeReports.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this UpgradeReports.

        升级开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param start_time: The start_time of this UpgradeReports.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this UpgradeReports.

        升级结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The end_time of this UpgradeReports.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this UpgradeReports.

        升级结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param end_time: The end_time of this UpgradeReports.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def src_instance_id(self):
        r"""Gets the src_instance_id of this UpgradeReports.

        原实例ID。

        :return: The src_instance_id of this UpgradeReports.
        :rtype: str
        """
        return self._src_instance_id

    @src_instance_id.setter
    def src_instance_id(self, src_instance_id):
        r"""Sets the src_instance_id of this UpgradeReports.

        原实例ID。

        :param src_instance_id: The src_instance_id of this UpgradeReports.
        :type src_instance_id: str
        """
        self._src_instance_id = src_instance_id

    @property
    def src_database_version(self):
        r"""Gets the src_database_version of this UpgradeReports.

        原数据库版本。

        :return: The src_database_version of this UpgradeReports.
        :rtype: str
        """
        return self._src_database_version

    @src_database_version.setter
    def src_database_version(self, src_database_version):
        r"""Sets the src_database_version of this UpgradeReports.

        原数据库版本。

        :param src_database_version: The src_database_version of this UpgradeReports.
        :type src_database_version: str
        """
        self._src_database_version = src_database_version

    @property
    def dst_instance_id(self):
        r"""Gets the dst_instance_id of this UpgradeReports.

        目标实例ID。

        :return: The dst_instance_id of this UpgradeReports.
        :rtype: str
        """
        return self._dst_instance_id

    @dst_instance_id.setter
    def dst_instance_id(self, dst_instance_id):
        r"""Sets the dst_instance_id of this UpgradeReports.

        目标实例ID。

        :param dst_instance_id: The dst_instance_id of this UpgradeReports.
        :type dst_instance_id: str
        """
        self._dst_instance_id = dst_instance_id

    @property
    def dst_database_version(self):
        r"""Gets the dst_database_version of this UpgradeReports.

        目标数据库版本。

        :return: The dst_database_version of this UpgradeReports.
        :rtype: str
        """
        return self._dst_database_version

    @dst_database_version.setter
    def dst_database_version(self, dst_database_version):
        r"""Sets the dst_database_version of this UpgradeReports.

        目标数据库版本。

        :param dst_database_version: The dst_database_version of this UpgradeReports.
        :type dst_database_version: str
        """
        self._dst_database_version = dst_database_version

    @property
    def result(self):
        r"""Gets the result of this UpgradeReports.

        升级结果。 success，表示成功。 failed，表示失败。 running， 表示升级中。

        :return: The result of this UpgradeReports.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this UpgradeReports.

        升级结果。 success，表示成功。 failed，表示失败。 running， 表示升级中。

        :param result: The result of this UpgradeReports.
        :type result: str
        """
        self._result = result

    @property
    def is_private_ip_changed(self):
        r"""Gets the is_private_ip_changed of this UpgradeReports.

        实例内网IP是否改变。 true，表示改变。 false，表示不改变。

        :return: The is_private_ip_changed of this UpgradeReports.
        :rtype: bool
        """
        return self._is_private_ip_changed

    @is_private_ip_changed.setter
    def is_private_ip_changed(self, is_private_ip_changed):
        r"""Sets the is_private_ip_changed of this UpgradeReports.

        实例内网IP是否改变。 true，表示改变。 false，表示不改变。

        :param is_private_ip_changed: The is_private_ip_changed of this UpgradeReports.
        :type is_private_ip_changed: bool
        """
        self._is_private_ip_changed = is_private_ip_changed

    @property
    def private_ip_change_time(self):
        r"""Gets the private_ip_change_time of this UpgradeReports.

        实例内网IP修改时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The private_ip_change_time of this UpgradeReports.
        :rtype: str
        """
        return self._private_ip_change_time

    @private_ip_change_time.setter
    def private_ip_change_time(self, private_ip_change_time):
        r"""Sets the private_ip_change_time of this UpgradeReports.

        实例内网IP修改时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param private_ip_change_time: The private_ip_change_time of this UpgradeReports.
        :type private_ip_change_time: str
        """
        self._private_ip_change_time = private_ip_change_time

    @property
    def statistics_collection_mode(self):
        r"""Gets the statistics_collection_mode of this UpgradeReports.

        统计信息收集模式。 before_change_private_ip，修改实例内网IP前收集。 after_change_private_ip，修改实例内网IP后收集。

        :return: The statistics_collection_mode of this UpgradeReports.
        :rtype: str
        """
        return self._statistics_collection_mode

    @statistics_collection_mode.setter
    def statistics_collection_mode(self, statistics_collection_mode):
        r"""Sets the statistics_collection_mode of this UpgradeReports.

        统计信息收集模式。 before_change_private_ip，修改实例内网IP前收集。 after_change_private_ip，修改实例内网IP后收集。

        :param statistics_collection_mode: The statistics_collection_mode of this UpgradeReports.
        :type statistics_collection_mode: str
        """
        self._statistics_collection_mode = statistics_collection_mode

    @property
    def detail(self):
        r"""Gets the detail of this UpgradeReports.

        升级报告详情。

        :return: The detail of this UpgradeReports.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this UpgradeReports.

        升级报告详情。

        :param detail: The detail of this UpgradeReports.
        :type detail: str
        """
        self._detail = detail

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
        if not isinstance(other, UpgradeReports):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
