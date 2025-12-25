# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecGuardTaskCount:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task': 'int',
        'artifact': 'int',
        'opensource': 'OpensourceCount',
        'virus': 'int',
        'malware': 'MalwareCount',
        'total': 'int',
        'list': 'list[SecGuardTaskDetail]'
    }

    attribute_map = {
        'task': 'task',
        'artifact': 'artifact',
        'opensource': 'opensource',
        'virus': 'virus',
        'malware': 'malware',
        'total': 'total',
        'list': 'list'
    }

    def __init__(self, task=None, artifact=None, opensource=None, virus=None, malware=None, total=None, list=None):
        r"""SecGuardTaskCount

        The model defined in huaweicloud sdk

        :param task: **参数解释**: 扫描次数。 **取值范围**: 不涉及。
        :type task: int
        :param artifact: **参数解释**: 扫描制品数。 **取值范围**: 不涉及。
        :type artifact: int
        :param opensource: 
        :type opensource: :class:`huaweicloudsdkcodeartsartifact.v2.OpensourceCount`
        :param virus: **参数解释**: 病毒文件数。 **取值范围**: 不涉及。
        :type virus: int
        :param malware: 
        :type malware: :class:`huaweicloudsdkcodeartsartifact.v2.MalwareCount`
        :param total: **参数解释**: 扫描总数。 **取值范围**: 不涉及。
        :type total: int
        :param list: **参数解释**: 扫描任务列表。 **取值范围**: 不涉及。
        :type list: list[:class:`huaweicloudsdkcodeartsartifact.v2.SecGuardTaskDetail`]
        """
        
        

        self._task = None
        self._artifact = None
        self._opensource = None
        self._virus = None
        self._malware = None
        self._total = None
        self._list = None
        self.discriminator = None

        if task is not None:
            self.task = task
        if artifact is not None:
            self.artifact = artifact
        if opensource is not None:
            self.opensource = opensource
        if virus is not None:
            self.virus = virus
        if malware is not None:
            self.malware = malware
        if total is not None:
            self.total = total
        if list is not None:
            self.list = list

    @property
    def task(self):
        r"""Gets the task of this SecGuardTaskCount.

        **参数解释**: 扫描次数。 **取值范围**: 不涉及。

        :return: The task of this SecGuardTaskCount.
        :rtype: int
        """
        return self._task

    @task.setter
    def task(self, task):
        r"""Sets the task of this SecGuardTaskCount.

        **参数解释**: 扫描次数。 **取值范围**: 不涉及。

        :param task: The task of this SecGuardTaskCount.
        :type task: int
        """
        self._task = task

    @property
    def artifact(self):
        r"""Gets the artifact of this SecGuardTaskCount.

        **参数解释**: 扫描制品数。 **取值范围**: 不涉及。

        :return: The artifact of this SecGuardTaskCount.
        :rtype: int
        """
        return self._artifact

    @artifact.setter
    def artifact(self, artifact):
        r"""Sets the artifact of this SecGuardTaskCount.

        **参数解释**: 扫描制品数。 **取值范围**: 不涉及。

        :param artifact: The artifact of this SecGuardTaskCount.
        :type artifact: int
        """
        self._artifact = artifact

    @property
    def opensource(self):
        r"""Gets the opensource of this SecGuardTaskCount.

        :return: The opensource of this SecGuardTaskCount.
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.OpensourceCount`
        """
        return self._opensource

    @opensource.setter
    def opensource(self, opensource):
        r"""Sets the opensource of this SecGuardTaskCount.

        :param opensource: The opensource of this SecGuardTaskCount.
        :type opensource: :class:`huaweicloudsdkcodeartsartifact.v2.OpensourceCount`
        """
        self._opensource = opensource

    @property
    def virus(self):
        r"""Gets the virus of this SecGuardTaskCount.

        **参数解释**: 病毒文件数。 **取值范围**: 不涉及。

        :return: The virus of this SecGuardTaskCount.
        :rtype: int
        """
        return self._virus

    @virus.setter
    def virus(self, virus):
        r"""Sets the virus of this SecGuardTaskCount.

        **参数解释**: 病毒文件数。 **取值范围**: 不涉及。

        :param virus: The virus of this SecGuardTaskCount.
        :type virus: int
        """
        self._virus = virus

    @property
    def malware(self):
        r"""Gets the malware of this SecGuardTaskCount.

        :return: The malware of this SecGuardTaskCount.
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.MalwareCount`
        """
        return self._malware

    @malware.setter
    def malware(self, malware):
        r"""Sets the malware of this SecGuardTaskCount.

        :param malware: The malware of this SecGuardTaskCount.
        :type malware: :class:`huaweicloudsdkcodeartsartifact.v2.MalwareCount`
        """
        self._malware = malware

    @property
    def total(self):
        r"""Gets the total of this SecGuardTaskCount.

        **参数解释**: 扫描总数。 **取值范围**: 不涉及。

        :return: The total of this SecGuardTaskCount.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this SecGuardTaskCount.

        **参数解释**: 扫描总数。 **取值范围**: 不涉及。

        :param total: The total of this SecGuardTaskCount.
        :type total: int
        """
        self._total = total

    @property
    def list(self):
        r"""Gets the list of this SecGuardTaskCount.

        **参数解释**: 扫描任务列表。 **取值范围**: 不涉及。

        :return: The list of this SecGuardTaskCount.
        :rtype: list[:class:`huaweicloudsdkcodeartsartifact.v2.SecGuardTaskDetail`]
        """
        return self._list

    @list.setter
    def list(self, list):
        r"""Sets the list of this SecGuardTaskCount.

        **参数解释**: 扫描任务列表。 **取值范围**: 不涉及。

        :param list: The list of this SecGuardTaskCount.
        :type list: list[:class:`huaweicloudsdkcodeartsartifact.v2.SecGuardTaskDetail`]
        """
        self._list = list

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SecGuardTaskCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
