# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoObjectMaskingInference:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pass_through': 'str',
        'scene_type': 'str',
        'outcome_name': 'str'
    }

    attribute_map = {
        'pass_through': 'pass_through',
        'scene_type': 'scene_type',
        'outcome_name': 'outcome_name'
    }

    def __init__(self, pass_through=None, scene_type=None, outcome_name=None):
        """VideoObjectMaskingInference

        The model defined in huaweicloud sdk

        :param pass_through: 透传客户信息
        :type pass_through: str
        :param scene_type: 擦除场景，可选车内或车外场景【inside,outside】
        :type scene_type: str
        :param outcome_name: 用户自定义产物名，无此项输入时，输出路径为{output结构体中指定输出path}/{task_id}/{task_id}.mp4；有此项输入时，输出路径为{output结构体中指定输出path}/{outcome_name}.mp4，自定义产物路径最多可定义5层文件夹目录。
        :type outcome_name: str
        """
        
        

        self._pass_through = None
        self._scene_type = None
        self._outcome_name = None
        self.discriminator = None

        if pass_through is not None:
            self.pass_through = pass_through
        self.scene_type = scene_type
        if outcome_name is not None:
            self.outcome_name = outcome_name

    @property
    def pass_through(self):
        """Gets the pass_through of this VideoObjectMaskingInference.

        透传客户信息

        :return: The pass_through of this VideoObjectMaskingInference.
        :rtype: str
        """
        return self._pass_through

    @pass_through.setter
    def pass_through(self, pass_through):
        """Sets the pass_through of this VideoObjectMaskingInference.

        透传客户信息

        :param pass_through: The pass_through of this VideoObjectMaskingInference.
        :type pass_through: str
        """
        self._pass_through = pass_through

    @property
    def scene_type(self):
        """Gets the scene_type of this VideoObjectMaskingInference.

        擦除场景，可选车内或车外场景【inside,outside】

        :return: The scene_type of this VideoObjectMaskingInference.
        :rtype: str
        """
        return self._scene_type

    @scene_type.setter
    def scene_type(self, scene_type):
        """Sets the scene_type of this VideoObjectMaskingInference.

        擦除场景，可选车内或车外场景【inside,outside】

        :param scene_type: The scene_type of this VideoObjectMaskingInference.
        :type scene_type: str
        """
        self._scene_type = scene_type

    @property
    def outcome_name(self):
        """Gets the outcome_name of this VideoObjectMaskingInference.

        用户自定义产物名，无此项输入时，输出路径为{output结构体中指定输出path}/{task_id}/{task_id}.mp4；有此项输入时，输出路径为{output结构体中指定输出path}/{outcome_name}.mp4，自定义产物路径最多可定义5层文件夹目录。

        :return: The outcome_name of this VideoObjectMaskingInference.
        :rtype: str
        """
        return self._outcome_name

    @outcome_name.setter
    def outcome_name(self, outcome_name):
        """Sets the outcome_name of this VideoObjectMaskingInference.

        用户自定义产物名，无此项输入时，输出路径为{output结构体中指定输出path}/{task_id}/{task_id}.mp4；有此项输入时，输出路径为{output结构体中指定输出path}/{outcome_name}.mp4，自定义产物路径最多可定义5层文件夹目录。

        :param outcome_name: The outcome_name of this VideoObjectMaskingInference.
        :type outcome_name: str
        """
        self._outcome_name = outcome_name

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
        if not isinstance(other, VideoObjectMaskingInference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
