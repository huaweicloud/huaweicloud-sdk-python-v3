# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryRepairDetailRespRepairDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_meta': 'str',
        'target_meta': 'str',
        'repair_sql_state': 'int',
        'repair_sql_info': 'str'
    }

    attribute_map = {
        'source_meta': 'source_meta',
        'target_meta': 'target_meta',
        'repair_sql_state': 'repair_sql_state',
        'repair_sql_info': 'repair_sql_info'
    }

    def __init__(self, source_meta=None, target_meta=None, repair_sql_state=None, repair_sql_info=None):
        r"""QueryRepairDetailRespRepairDetails

        The model defined in huaweicloud sdk

        :param source_meta: 源表标志列值。
        :type source_meta: str
        :param target_meta: 目标表标志列值。
        :type target_meta: str
        :param repair_sql_state: 修复SQL状态。
        :type repair_sql_state: int
        :param repair_sql_info: 修复SQL。
        :type repair_sql_info: str
        """
        
        

        self._source_meta = None
        self._target_meta = None
        self._repair_sql_state = None
        self._repair_sql_info = None
        self.discriminator = None

        if source_meta is not None:
            self.source_meta = source_meta
        if target_meta is not None:
            self.target_meta = target_meta
        if repair_sql_state is not None:
            self.repair_sql_state = repair_sql_state
        if repair_sql_info is not None:
            self.repair_sql_info = repair_sql_info

    @property
    def source_meta(self):
        r"""Gets the source_meta of this QueryRepairDetailRespRepairDetails.

        源表标志列值。

        :return: The source_meta of this QueryRepairDetailRespRepairDetails.
        :rtype: str
        """
        return self._source_meta

    @source_meta.setter
    def source_meta(self, source_meta):
        r"""Sets the source_meta of this QueryRepairDetailRespRepairDetails.

        源表标志列值。

        :param source_meta: The source_meta of this QueryRepairDetailRespRepairDetails.
        :type source_meta: str
        """
        self._source_meta = source_meta

    @property
    def target_meta(self):
        r"""Gets the target_meta of this QueryRepairDetailRespRepairDetails.

        目标表标志列值。

        :return: The target_meta of this QueryRepairDetailRespRepairDetails.
        :rtype: str
        """
        return self._target_meta

    @target_meta.setter
    def target_meta(self, target_meta):
        r"""Sets the target_meta of this QueryRepairDetailRespRepairDetails.

        目标表标志列值。

        :param target_meta: The target_meta of this QueryRepairDetailRespRepairDetails.
        :type target_meta: str
        """
        self._target_meta = target_meta

    @property
    def repair_sql_state(self):
        r"""Gets the repair_sql_state of this QueryRepairDetailRespRepairDetails.

        修复SQL状态。

        :return: The repair_sql_state of this QueryRepairDetailRespRepairDetails.
        :rtype: int
        """
        return self._repair_sql_state

    @repair_sql_state.setter
    def repair_sql_state(self, repair_sql_state):
        r"""Sets the repair_sql_state of this QueryRepairDetailRespRepairDetails.

        修复SQL状态。

        :param repair_sql_state: The repair_sql_state of this QueryRepairDetailRespRepairDetails.
        :type repair_sql_state: int
        """
        self._repair_sql_state = repair_sql_state

    @property
    def repair_sql_info(self):
        r"""Gets the repair_sql_info of this QueryRepairDetailRespRepairDetails.

        修复SQL。

        :return: The repair_sql_info of this QueryRepairDetailRespRepairDetails.
        :rtype: str
        """
        return self._repair_sql_info

    @repair_sql_info.setter
    def repair_sql_info(self, repair_sql_info):
        r"""Sets the repair_sql_info of this QueryRepairDetailRespRepairDetails.

        修复SQL。

        :param repair_sql_info: The repair_sql_info of this QueryRepairDetailRespRepairDetails.
        :type repair_sql_info: str
        """
        self._repair_sql_info = repair_sql_info

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
        if not isinstance(other, QueryRepairDetailRespRepairDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
