# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEditingJobsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'inputs': 'list[EditingInput]',
        'output': 'ObsObjInfo',
        'editing_settings': 'EditingSetting',
        'user_data': 'str'
    }

    attribute_map = {
        'inputs': 'inputs',
        'output': 'output',
        'editing_settings': 'editing_settings',
        'user_data': 'user_data'
    }

    def __init__(self, inputs=None, output=None, editing_settings=None, user_data=None):
        """CreateEditingJobsReq

        The model defined in huaweicloud sdk

        :param inputs: 指定片源多个剪切时间段
        :type inputs: list[:class:`huaweicloudsdkmpc.v1.EditingInput`]
        :param output: 
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        :param editing_settings: 
        :type editing_settings: :class:`huaweicloudsdkmpc.v1.EditingSetting`
        :param user_data: 用户自定义数据
        :type user_data: str
        """
        
        

        self._inputs = None
        self._output = None
        self._editing_settings = None
        self._user_data = None
        self.discriminator = None

        if inputs is not None:
            self.inputs = inputs
        if output is not None:
            self.output = output
        if editing_settings is not None:
            self.editing_settings = editing_settings
        if user_data is not None:
            self.user_data = user_data

    @property
    def inputs(self):
        """Gets the inputs of this CreateEditingJobsReq.

        指定片源多个剪切时间段

        :return: The inputs of this CreateEditingJobsReq.
        :rtype: list[:class:`huaweicloudsdkmpc.v1.EditingInput`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this CreateEditingJobsReq.

        指定片源多个剪切时间段

        :param inputs: The inputs of this CreateEditingJobsReq.
        :type inputs: list[:class:`huaweicloudsdkmpc.v1.EditingInput`]
        """
        self._inputs = inputs

    @property
    def output(self):
        """Gets the output of this CreateEditingJobsReq.

        :return: The output of this CreateEditingJobsReq.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this CreateEditingJobsReq.

        :param output: The output of this CreateEditingJobsReq.
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._output = output

    @property
    def editing_settings(self):
        """Gets the editing_settings of this CreateEditingJobsReq.

        :return: The editing_settings of this CreateEditingJobsReq.
        :rtype: :class:`huaweicloudsdkmpc.v1.EditingSetting`
        """
        return self._editing_settings

    @editing_settings.setter
    def editing_settings(self, editing_settings):
        """Sets the editing_settings of this CreateEditingJobsReq.

        :param editing_settings: The editing_settings of this CreateEditingJobsReq.
        :type editing_settings: :class:`huaweicloudsdkmpc.v1.EditingSetting`
        """
        self._editing_settings = editing_settings

    @property
    def user_data(self):
        """Gets the user_data of this CreateEditingJobsReq.

        用户自定义数据

        :return: The user_data of this CreateEditingJobsReq.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this CreateEditingJobsReq.

        用户自定义数据

        :param user_data: The user_data of this CreateEditingJobsReq.
        :type user_data: str
        """
        self._user_data = user_data

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
        if not isinstance(other, CreateEditingJobsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
