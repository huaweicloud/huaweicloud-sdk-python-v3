# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDataLevelCompareReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'conflict_policy': 'str',
        'compare_type': 'str',
        'compare_mode': 'str',
        'start_time': 'str',
        'compare_object_infos': 'list[CompareObjectInfo]',
        'compare_object_infos_with_token': 'list[CompareObjectInfoWithToken]'
    }

    attribute_map = {
        'conflict_policy': 'conflict_policy',
        'compare_type': 'compare_type',
        'compare_mode': 'compare_mode',
        'start_time': 'start_time',
        'compare_object_infos': 'compare_object_infos',
        'compare_object_infos_with_token': 'compare_object_infos_with_token'
    }

    def __init__(self, conflict_policy=None, compare_type=None, compare_mode=None, start_time=None, compare_object_infos=None, compare_object_infos_with_token=None):
        """CreateDataLevelCompareReq

        The model defined in huaweicloud sdk

        :param conflict_policy: 一个任务只允许有一个未完成的数据级对比任务，该字段决定对未完成数据级对比任务的处理方式。cancel-取消后重新创建,keep-保持未完成的不再创建。
        :type conflict_policy: str
        :param compare_type: 数据级对比类型，lines-行对比,contents-内容对比。
        :type compare_type: str
        :param compare_mode: 数据级对比模式，取值为空时需要在compare_object_infos或者compare_object_infos_with_token传对象信息，quick_comparison-快速对比，需要加入该功能的白名单才能使用。
        :type compare_mode: str
        :param start_time: 对比任务启动时间，取值为空代表立即启动。
        :type start_time: str
        :param compare_object_infos: 数据级对比的对象。非“快速对比”模式时，compare_object_infos和compare_object_infos_with_token根据链路二选一传值，不允许都为空。
        :type compare_object_infos: list[:class:`huaweicloudsdkdrs.v3.CompareObjectInfo`]
        :param compare_object_infos_with_token: 数据级对比的对象（Cassandra灾备专用，带token信息）。非“快速对比”模式时，compare_object_infos和compare_object_infos_with_token根据链路二选一传值，不允许都为空。
        :type compare_object_infos_with_token: list[:class:`huaweicloudsdkdrs.v3.CompareObjectInfoWithToken`]
        """
        
        

        self._conflict_policy = None
        self._compare_type = None
        self._compare_mode = None
        self._start_time = None
        self._compare_object_infos = None
        self._compare_object_infos_with_token = None
        self.discriminator = None

        self.conflict_policy = conflict_policy
        self.compare_type = compare_type
        if compare_mode is not None:
            self.compare_mode = compare_mode
        if start_time is not None:
            self.start_time = start_time
        if compare_object_infos is not None:
            self.compare_object_infos = compare_object_infos
        if compare_object_infos_with_token is not None:
            self.compare_object_infos_with_token = compare_object_infos_with_token

    @property
    def conflict_policy(self):
        """Gets the conflict_policy of this CreateDataLevelCompareReq.

        一个任务只允许有一个未完成的数据级对比任务，该字段决定对未完成数据级对比任务的处理方式。cancel-取消后重新创建,keep-保持未完成的不再创建。

        :return: The conflict_policy of this CreateDataLevelCompareReq.
        :rtype: str
        """
        return self._conflict_policy

    @conflict_policy.setter
    def conflict_policy(self, conflict_policy):
        """Sets the conflict_policy of this CreateDataLevelCompareReq.

        一个任务只允许有一个未完成的数据级对比任务，该字段决定对未完成数据级对比任务的处理方式。cancel-取消后重新创建,keep-保持未完成的不再创建。

        :param conflict_policy: The conflict_policy of this CreateDataLevelCompareReq.
        :type conflict_policy: str
        """
        self._conflict_policy = conflict_policy

    @property
    def compare_type(self):
        """Gets the compare_type of this CreateDataLevelCompareReq.

        数据级对比类型，lines-行对比,contents-内容对比。

        :return: The compare_type of this CreateDataLevelCompareReq.
        :rtype: str
        """
        return self._compare_type

    @compare_type.setter
    def compare_type(self, compare_type):
        """Sets the compare_type of this CreateDataLevelCompareReq.

        数据级对比类型，lines-行对比,contents-内容对比。

        :param compare_type: The compare_type of this CreateDataLevelCompareReq.
        :type compare_type: str
        """
        self._compare_type = compare_type

    @property
    def compare_mode(self):
        """Gets the compare_mode of this CreateDataLevelCompareReq.

        数据级对比模式，取值为空时需要在compare_object_infos或者compare_object_infos_with_token传对象信息，quick_comparison-快速对比，需要加入该功能的白名单才能使用。

        :return: The compare_mode of this CreateDataLevelCompareReq.
        :rtype: str
        """
        return self._compare_mode

    @compare_mode.setter
    def compare_mode(self, compare_mode):
        """Sets the compare_mode of this CreateDataLevelCompareReq.

        数据级对比模式，取值为空时需要在compare_object_infos或者compare_object_infos_with_token传对象信息，quick_comparison-快速对比，需要加入该功能的白名单才能使用。

        :param compare_mode: The compare_mode of this CreateDataLevelCompareReq.
        :type compare_mode: str
        """
        self._compare_mode = compare_mode

    @property
    def start_time(self):
        """Gets the start_time of this CreateDataLevelCompareReq.

        对比任务启动时间，取值为空代表立即启动。

        :return: The start_time of this CreateDataLevelCompareReq.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this CreateDataLevelCompareReq.

        对比任务启动时间，取值为空代表立即启动。

        :param start_time: The start_time of this CreateDataLevelCompareReq.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def compare_object_infos(self):
        """Gets the compare_object_infos of this CreateDataLevelCompareReq.

        数据级对比的对象。非“快速对比”模式时，compare_object_infos和compare_object_infos_with_token根据链路二选一传值，不允许都为空。

        :return: The compare_object_infos of this CreateDataLevelCompareReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.CompareObjectInfo`]
        """
        return self._compare_object_infos

    @compare_object_infos.setter
    def compare_object_infos(self, compare_object_infos):
        """Sets the compare_object_infos of this CreateDataLevelCompareReq.

        数据级对比的对象。非“快速对比”模式时，compare_object_infos和compare_object_infos_with_token根据链路二选一传值，不允许都为空。

        :param compare_object_infos: The compare_object_infos of this CreateDataLevelCompareReq.
        :type compare_object_infos: list[:class:`huaweicloudsdkdrs.v3.CompareObjectInfo`]
        """
        self._compare_object_infos = compare_object_infos

    @property
    def compare_object_infos_with_token(self):
        """Gets the compare_object_infos_with_token of this CreateDataLevelCompareReq.

        数据级对比的对象（Cassandra灾备专用，带token信息）。非“快速对比”模式时，compare_object_infos和compare_object_infos_with_token根据链路二选一传值，不允许都为空。

        :return: The compare_object_infos_with_token of this CreateDataLevelCompareReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.CompareObjectInfoWithToken`]
        """
        return self._compare_object_infos_with_token

    @compare_object_infos_with_token.setter
    def compare_object_infos_with_token(self, compare_object_infos_with_token):
        """Sets the compare_object_infos_with_token of this CreateDataLevelCompareReq.

        数据级对比的对象（Cassandra灾备专用，带token信息）。非“快速对比”模式时，compare_object_infos和compare_object_infos_with_token根据链路二选一传值，不允许都为空。

        :param compare_object_infos_with_token: The compare_object_infos_with_token of this CreateDataLevelCompareReq.
        :type compare_object_infos_with_token: list[:class:`huaweicloudsdkdrs.v3.CompareObjectInfoWithToken`]
        """
        self._compare_object_infos_with_token = compare_object_infos_with_token

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
        if not isinstance(other, CreateDataLevelCompareReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
