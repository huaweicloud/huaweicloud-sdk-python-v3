# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobBaselineInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'job_name': 'str',
        'baselines': 'list[BaselineInfo]'
    }

    attribute_map = {
        'job_id': 'job_id',
        'job_name': 'job_name',
        'baselines': 'baselines'
    }

    def __init__(self, job_id=None, job_name=None, baselines=None):
        r"""JobBaselineInfo

        The model defined in huaweicloud sdk

        :param job_id: **参数解释**： 作业ID。 **取值范围**： 长度为1~64个字符。
        :type job_id: str
        :param job_name: **参数解释**： 作业名称。如果作业不存在或不在当前工作空间内，则为空。 **取值范围**： 长度为1~1024个字符。
        :type job_name: str
        :param baselines: **参数解释**： 作业关联的基线信息列表。如果作业未关联基线，则返回空列表。 **取值范围**： 不涉及。
        :type baselines: list[:class:`huaweicloudsdkdataartsstudio.v1.BaselineInfo`]
        """
        
        

        self._job_id = None
        self._job_name = None
        self._baselines = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if job_name is not None:
            self.job_name = job_name
        if baselines is not None:
            self.baselines = baselines

    @property
    def job_id(self):
        r"""Gets the job_id of this JobBaselineInfo.

        **参数解释**： 作业ID。 **取值范围**： 长度为1~64个字符。

        :return: The job_id of this JobBaselineInfo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this JobBaselineInfo.

        **参数解释**： 作业ID。 **取值范围**： 长度为1~64个字符。

        :param job_id: The job_id of this JobBaselineInfo.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        r"""Gets the job_name of this JobBaselineInfo.

        **参数解释**： 作业名称。如果作业不存在或不在当前工作空间内，则为空。 **取值范围**： 长度为1~1024个字符。

        :return: The job_name of this JobBaselineInfo.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this JobBaselineInfo.

        **参数解释**： 作业名称。如果作业不存在或不在当前工作空间内，则为空。 **取值范围**： 长度为1~1024个字符。

        :param job_name: The job_name of this JobBaselineInfo.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def baselines(self):
        r"""Gets the baselines of this JobBaselineInfo.

        **参数解释**： 作业关联的基线信息列表。如果作业未关联基线，则返回空列表。 **取值范围**： 不涉及。

        :return: The baselines of this JobBaselineInfo.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.BaselineInfo`]
        """
        return self._baselines

    @baselines.setter
    def baselines(self, baselines):
        r"""Sets the baselines of this JobBaselineInfo.

        **参数解释**： 作业关联的基线信息列表。如果作业未关联基线，则返回空列表。 **取值范围**： 不涉及。

        :param baselines: The baselines of this JobBaselineInfo.
        :type baselines: list[:class:`huaweicloudsdkdataartsstudio.v1.BaselineInfo`]
        """
        self._baselines = baselines

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
        if not isinstance(other, JobBaselineInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
