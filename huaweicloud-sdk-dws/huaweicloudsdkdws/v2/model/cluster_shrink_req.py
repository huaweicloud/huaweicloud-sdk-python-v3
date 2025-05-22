# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterShrinkReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'shrink_number': 'int',
        'online': 'bool',
        'retry': 'bool',
        'need_agency': 'bool',
        'parallel_jobs': 'int',
        'type': 'str',
        'force_backup': 'bool'
    }

    attribute_map = {
        'shrink_number': 'shrink_number',
        'online': 'online',
        'retry': 'retry',
        'need_agency': 'need_agency',
        'parallel_jobs': 'parallel_jobs',
        'type': 'type',
        'force_backup': 'force_backup'
    }

    def __init__(self, shrink_number=None, online=None, retry=None, need_agency=None, parallel_jobs=None, type=None, force_backup=None):
        r"""ClusterShrinkReq

        The model defined in huaweicloud sdk

        :param shrink_number: **参数解释**：  缩容节点个数。  **约束限制**：  该值不能为空。  **取值范围**：  大于0的整数。  **默认取值**：  不涉及。
        :type shrink_number: int
        :param online: **参数解释**：  是否是在线缩容。  **约束限制**：  不涉及。  **取值范围**：  false|true。  **默认取值**：  false。
        :type online: bool
        :param retry: **参数解释**：  是否是缩容失败后重试。  **约束限制**：  不涉及。  **取值范围**：  false|true。  **默认取值**：  false。
        :type retry: bool
        :param need_agency: **参数解释**：  是否需要委托。  **约束限制**：  不涉及。  **取值范围**：  false或true。  **默认取值**：  false。
        :type need_agency: bool
        :param parallel_jobs: **参数解释**：  重分布并发配置数。  **约束限制**：  不涉及。  **取值范围**：  1~200。  **默认取值**：  4。
        :type parallel_jobs: int
        :param type: **参数解释**：  类型字段，字段已废弃不再生效。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type type: str
        :param force_backup: **参数解释**：  操作前是否执行备份，字段已废弃不再生效。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type force_backup: bool
        """
        
        

        self._shrink_number = None
        self._online = None
        self._retry = None
        self._need_agency = None
        self._parallel_jobs = None
        self._type = None
        self._force_backup = None
        self.discriminator = None

        if shrink_number is not None:
            self.shrink_number = shrink_number
        if online is not None:
            self.online = online
        if retry is not None:
            self.retry = retry
        if need_agency is not None:
            self.need_agency = need_agency
        if parallel_jobs is not None:
            self.parallel_jobs = parallel_jobs
        if type is not None:
            self.type = type
        if force_backup is not None:
            self.force_backup = force_backup

    @property
    def shrink_number(self):
        r"""Gets the shrink_number of this ClusterShrinkReq.

        **参数解释**：  缩容节点个数。  **约束限制**：  该值不能为空。  **取值范围**：  大于0的整数。  **默认取值**：  不涉及。

        :return: The shrink_number of this ClusterShrinkReq.
        :rtype: int
        """
        return self._shrink_number

    @shrink_number.setter
    def shrink_number(self, shrink_number):
        r"""Sets the shrink_number of this ClusterShrinkReq.

        **参数解释**：  缩容节点个数。  **约束限制**：  该值不能为空。  **取值范围**：  大于0的整数。  **默认取值**：  不涉及。

        :param shrink_number: The shrink_number of this ClusterShrinkReq.
        :type shrink_number: int
        """
        self._shrink_number = shrink_number

    @property
    def online(self):
        r"""Gets the online of this ClusterShrinkReq.

        **参数解释**：  是否是在线缩容。  **约束限制**：  不涉及。  **取值范围**：  false|true。  **默认取值**：  false。

        :return: The online of this ClusterShrinkReq.
        :rtype: bool
        """
        return self._online

    @online.setter
    def online(self, online):
        r"""Sets the online of this ClusterShrinkReq.

        **参数解释**：  是否是在线缩容。  **约束限制**：  不涉及。  **取值范围**：  false|true。  **默认取值**：  false。

        :param online: The online of this ClusterShrinkReq.
        :type online: bool
        """
        self._online = online

    @property
    def retry(self):
        r"""Gets the retry of this ClusterShrinkReq.

        **参数解释**：  是否是缩容失败后重试。  **约束限制**：  不涉及。  **取值范围**：  false|true。  **默认取值**：  false。

        :return: The retry of this ClusterShrinkReq.
        :rtype: bool
        """
        return self._retry

    @retry.setter
    def retry(self, retry):
        r"""Sets the retry of this ClusterShrinkReq.

        **参数解释**：  是否是缩容失败后重试。  **约束限制**：  不涉及。  **取值范围**：  false|true。  **默认取值**：  false。

        :param retry: The retry of this ClusterShrinkReq.
        :type retry: bool
        """
        self._retry = retry

    @property
    def need_agency(self):
        r"""Gets the need_agency of this ClusterShrinkReq.

        **参数解释**：  是否需要委托。  **约束限制**：  不涉及。  **取值范围**：  false或true。  **默认取值**：  false。

        :return: The need_agency of this ClusterShrinkReq.
        :rtype: bool
        """
        return self._need_agency

    @need_agency.setter
    def need_agency(self, need_agency):
        r"""Sets the need_agency of this ClusterShrinkReq.

        **参数解释**：  是否需要委托。  **约束限制**：  不涉及。  **取值范围**：  false或true。  **默认取值**：  false。

        :param need_agency: The need_agency of this ClusterShrinkReq.
        :type need_agency: bool
        """
        self._need_agency = need_agency

    @property
    def parallel_jobs(self):
        r"""Gets the parallel_jobs of this ClusterShrinkReq.

        **参数解释**：  重分布并发配置数。  **约束限制**：  不涉及。  **取值范围**：  1~200。  **默认取值**：  4。

        :return: The parallel_jobs of this ClusterShrinkReq.
        :rtype: int
        """
        return self._parallel_jobs

    @parallel_jobs.setter
    def parallel_jobs(self, parallel_jobs):
        r"""Sets the parallel_jobs of this ClusterShrinkReq.

        **参数解释**：  重分布并发配置数。  **约束限制**：  不涉及。  **取值范围**：  1~200。  **默认取值**：  4。

        :param parallel_jobs: The parallel_jobs of this ClusterShrinkReq.
        :type parallel_jobs: int
        """
        self._parallel_jobs = parallel_jobs

    @property
    def type(self):
        r"""Gets the type of this ClusterShrinkReq.

        **参数解释**：  类型字段，字段已废弃不再生效。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The type of this ClusterShrinkReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ClusterShrinkReq.

        **参数解释**：  类型字段，字段已废弃不再生效。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param type: The type of this ClusterShrinkReq.
        :type type: str
        """
        self._type = type

    @property
    def force_backup(self):
        r"""Gets the force_backup of this ClusterShrinkReq.

        **参数解释**：  操作前是否执行备份，字段已废弃不再生效。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The force_backup of this ClusterShrinkReq.
        :rtype: bool
        """
        return self._force_backup

    @force_backup.setter
    def force_backup(self, force_backup):
        r"""Sets the force_backup of this ClusterShrinkReq.

        **参数解释**：  操作前是否执行备份，字段已废弃不再生效。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param force_backup: The force_backup of this ClusterShrinkReq.
        :type force_backup: bool
        """
        self._force_backup = force_backup

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
        if not isinstance(other, ClusterShrinkReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
