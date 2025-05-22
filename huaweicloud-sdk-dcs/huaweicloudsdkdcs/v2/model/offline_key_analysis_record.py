# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OfflineKeyAnalysisRecord:

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
        'status': 'str',
        'created_at': 'str',
        'started_at': 'str',
        'finished_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'created_at': 'created_at',
        'started_at': 'started_at',
        'finished_at': 'finished_at'
    }

    def __init__(self, id=None, status=None, created_at=None, started_at=None, finished_at=None):
        r"""OfflineKeyAnalysisRecord

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 任务执行记录ID（此ID对应“查询离线全量key分析详情”参数中的任务ID）。 **取值范围**： 不涉及。 
        :type id: str
        :param status: **参数解释**： 离线分析任务状态。 **取值范围**： waiting：任务等待中。 running：任务进行中。 success：任务执行成功。 failed：任务执行失败。 
        :type status: str
        :param created_at: **参数解释**： 分析任务创建时间。 **取值范围**： 不涉及。 
        :type created_at: str
        :param started_at: **参数解释**： 分析任务开始时间。 **取值范围**： 不涉及。 
        :type started_at: str
        :param finished_at: **参数解释**： 分析任务结束时间。 **取值范围**： 不涉及。 
        :type finished_at: str
        """
        
        

        self._id = None
        self._status = None
        self._created_at = None
        self._started_at = None
        self._finished_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if started_at is not None:
            self.started_at = started_at
        if finished_at is not None:
            self.finished_at = finished_at

    @property
    def id(self):
        r"""Gets the id of this OfflineKeyAnalysisRecord.

        **参数解释**： 任务执行记录ID（此ID对应“查询离线全量key分析详情”参数中的任务ID）。 **取值范围**： 不涉及。 

        :return: The id of this OfflineKeyAnalysisRecord.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this OfflineKeyAnalysisRecord.

        **参数解释**： 任务执行记录ID（此ID对应“查询离线全量key分析详情”参数中的任务ID）。 **取值范围**： 不涉及。 

        :param id: The id of this OfflineKeyAnalysisRecord.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this OfflineKeyAnalysisRecord.

        **参数解释**： 离线分析任务状态。 **取值范围**： waiting：任务等待中。 running：任务进行中。 success：任务执行成功。 failed：任务执行失败。 

        :return: The status of this OfflineKeyAnalysisRecord.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this OfflineKeyAnalysisRecord.

        **参数解释**： 离线分析任务状态。 **取值范围**： waiting：任务等待中。 running：任务进行中。 success：任务执行成功。 failed：任务执行失败。 

        :param status: The status of this OfflineKeyAnalysisRecord.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this OfflineKeyAnalysisRecord.

        **参数解释**： 分析任务创建时间。 **取值范围**： 不涉及。 

        :return: The created_at of this OfflineKeyAnalysisRecord.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this OfflineKeyAnalysisRecord.

        **参数解释**： 分析任务创建时间。 **取值范围**： 不涉及。 

        :param created_at: The created_at of this OfflineKeyAnalysisRecord.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def started_at(self):
        r"""Gets the started_at of this OfflineKeyAnalysisRecord.

        **参数解释**： 分析任务开始时间。 **取值范围**： 不涉及。 

        :return: The started_at of this OfflineKeyAnalysisRecord.
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        r"""Sets the started_at of this OfflineKeyAnalysisRecord.

        **参数解释**： 分析任务开始时间。 **取值范围**： 不涉及。 

        :param started_at: The started_at of this OfflineKeyAnalysisRecord.
        :type started_at: str
        """
        self._started_at = started_at

    @property
    def finished_at(self):
        r"""Gets the finished_at of this OfflineKeyAnalysisRecord.

        **参数解释**： 分析任务结束时间。 **取值范围**： 不涉及。 

        :return: The finished_at of this OfflineKeyAnalysisRecord.
        :rtype: str
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        r"""Sets the finished_at of this OfflineKeyAnalysisRecord.

        **参数解释**： 分析任务结束时间。 **取值范围**： 不涉及。 

        :param finished_at: The finished_at of this OfflineKeyAnalysisRecord.
        :type finished_at: str
        """
        self._finished_at = finished_at

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
        if not isinstance(other, OfflineKeyAnalysisRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
