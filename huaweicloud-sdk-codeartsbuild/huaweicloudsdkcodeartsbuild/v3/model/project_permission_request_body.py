# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectPermissionRequestBody:

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
        'project_id': 'str',
        'project_switch': 'bool'
    }

    attribute_map = {
        'job_id': 'job_id',
        'project_id': 'project_id',
        'project_switch': 'project_switch'
    }

    def __init__(self, job_id=None, project_id=None, project_switch=None):
        r"""ProjectPermissionRequestBody

        The model defined in huaweicloud sdk

        :param job_id: **参数解释**： 填写需要查询构建历史列表的构建任务ID。获取方法：在构建任务详情页，拷贝浏览器URL末尾的32位数字、字母组合的字符串，即为构建任务ID。 **约束限制**： 不涉及。 **取值范围**： 只能是英文字母和数字，长度为32个字符。 **默认取值**： 不涉及。
        :type job_id: str
        :param project_id: **参数解释**： CodeArts项目ID。获取方式请参考[获取CodeArts项目ID](https://support.huaweicloud.com/api-codeci/cloudbuild_03_0022.html)。 **约束限制**： 不涉及。 **取值范围**： 32位数字、字母组合的字符串。 **默认取值**： 不涉及。
        :type project_id: str
        :param project_switch: **参数解释**： 是否同步最新一次项目权限。 **约束限制**： 不涉及。 **取值范围**： ● true：使用项目级权限。 ● false：不使用项目级权限。 **默认取值**： 不涉及。
        :type project_switch: bool
        """
        
        

        self._job_id = None
        self._project_id = None
        self._project_switch = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if project_id is not None:
            self.project_id = project_id
        if project_switch is not None:
            self.project_switch = project_switch

    @property
    def job_id(self):
        r"""Gets the job_id of this ProjectPermissionRequestBody.

        **参数解释**： 填写需要查询构建历史列表的构建任务ID。获取方法：在构建任务详情页，拷贝浏览器URL末尾的32位数字、字母组合的字符串，即为构建任务ID。 **约束限制**： 不涉及。 **取值范围**： 只能是英文字母和数字，长度为32个字符。 **默认取值**： 不涉及。

        :return: The job_id of this ProjectPermissionRequestBody.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ProjectPermissionRequestBody.

        **参数解释**： 填写需要查询构建历史列表的构建任务ID。获取方法：在构建任务详情页，拷贝浏览器URL末尾的32位数字、字母组合的字符串，即为构建任务ID。 **约束限制**： 不涉及。 **取值范围**： 只能是英文字母和数字，长度为32个字符。 **默认取值**： 不涉及。

        :param job_id: The job_id of this ProjectPermissionRequestBody.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ProjectPermissionRequestBody.

        **参数解释**： CodeArts项目ID。获取方式请参考[获取CodeArts项目ID](https://support.huaweicloud.com/api-codeci/cloudbuild_03_0022.html)。 **约束限制**： 不涉及。 **取值范围**： 32位数字、字母组合的字符串。 **默认取值**： 不涉及。

        :return: The project_id of this ProjectPermissionRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ProjectPermissionRequestBody.

        **参数解释**： CodeArts项目ID。获取方式请参考[获取CodeArts项目ID](https://support.huaweicloud.com/api-codeci/cloudbuild_03_0022.html)。 **约束限制**： 不涉及。 **取值范围**： 32位数字、字母组合的字符串。 **默认取值**： 不涉及。

        :param project_id: The project_id of this ProjectPermissionRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_switch(self):
        r"""Gets the project_switch of this ProjectPermissionRequestBody.

        **参数解释**： 是否同步最新一次项目权限。 **约束限制**： 不涉及。 **取值范围**： ● true：使用项目级权限。 ● false：不使用项目级权限。 **默认取值**： 不涉及。

        :return: The project_switch of this ProjectPermissionRequestBody.
        :rtype: bool
        """
        return self._project_switch

    @project_switch.setter
    def project_switch(self, project_switch):
        r"""Sets the project_switch of this ProjectPermissionRequestBody.

        **参数解释**： 是否同步最新一次项目权限。 **约束限制**： 不涉及。 **取值范围**： ● true：使用项目级权限。 ● false：不使用项目级权限。 **默认取值**： 不涉及。

        :param project_switch: The project_switch of this ProjectPermissionRequestBody.
        :type project_switch: bool
        """
        self._project_switch = project_switch

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
        if not isinstance(other, ProjectPermissionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
