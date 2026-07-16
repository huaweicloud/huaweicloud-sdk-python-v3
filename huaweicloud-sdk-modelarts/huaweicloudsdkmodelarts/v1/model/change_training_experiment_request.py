# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeTrainingExperimentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'experiment_id': 'str',
        'body': 'ChangeTrainingExperimentRequestBody'
    }

    attribute_map = {
        'experiment_id': 'experiment_id',
        'body': 'body'
    }

    def __init__(self, experiment_id=None, body=None):
        r"""ChangeTrainingExperimentRequest

        The model defined in huaweicloud sdk

        :param experiment_id: 训练实验ID。在训练作业创建时获取实验ID。
        :type experiment_id: str
        :param body: Body of the ChangeTrainingExperimentRequest
        :type body: :class:`huaweicloudsdkmodelarts.v1.ChangeTrainingExperimentRequestBody`
        """
        
        

        self._experiment_id = None
        self._body = None
        self.discriminator = None

        self.experiment_id = experiment_id
        if body is not None:
            self.body = body

    @property
    def experiment_id(self):
        r"""Gets the experiment_id of this ChangeTrainingExperimentRequest.

        训练实验ID。在训练作业创建时获取实验ID。

        :return: The experiment_id of this ChangeTrainingExperimentRequest.
        :rtype: str
        """
        return self._experiment_id

    @experiment_id.setter
    def experiment_id(self, experiment_id):
        r"""Sets the experiment_id of this ChangeTrainingExperimentRequest.

        训练实验ID。在训练作业创建时获取实验ID。

        :param experiment_id: The experiment_id of this ChangeTrainingExperimentRequest.
        :type experiment_id: str
        """
        self._experiment_id = experiment_id

    @property
    def body(self):
        r"""Gets the body of this ChangeTrainingExperimentRequest.

        :return: The body of this ChangeTrainingExperimentRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ChangeTrainingExperimentRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ChangeTrainingExperimentRequest.

        :param body: The body of this ChangeTrainingExperimentRequest.
        :type body: :class:`huaweicloudsdkmodelarts.v1.ChangeTrainingExperimentRequestBody`
        """
        self._body = body

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
        if not isinstance(other, ChangeTrainingExperimentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
