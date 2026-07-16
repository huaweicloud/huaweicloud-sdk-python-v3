# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTrainingExperimentDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metadata': 'TrainingExperimentResponseMetadata',
        'statistic': 'TrainingExperimentStatistic'
    }

    attribute_map = {
        'metadata': 'metadata',
        'statistic': 'statistic'
    }

    def __init__(self, metadata=None, statistic=None):
        r"""ShowTrainingExperimentDetailsResponse

        The model defined in huaweicloud sdk

        :param metadata: 
        :type metadata: :class:`huaweicloudsdkmodelarts.v1.TrainingExperimentResponseMetadata`
        :param statistic: 
        :type statistic: :class:`huaweicloudsdkmodelarts.v1.TrainingExperimentStatistic`
        """
        
        super().__init__()

        self._metadata = None
        self._statistic = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if statistic is not None:
            self.statistic = statistic

    @property
    def metadata(self):
        r"""Gets the metadata of this ShowTrainingExperimentDetailsResponse.

        :return: The metadata of this ShowTrainingExperimentDetailsResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.TrainingExperimentResponseMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ShowTrainingExperimentDetailsResponse.

        :param metadata: The metadata of this ShowTrainingExperimentDetailsResponse.
        :type metadata: :class:`huaweicloudsdkmodelarts.v1.TrainingExperimentResponseMetadata`
        """
        self._metadata = metadata

    @property
    def statistic(self):
        r"""Gets the statistic of this ShowTrainingExperimentDetailsResponse.

        :return: The statistic of this ShowTrainingExperimentDetailsResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.TrainingExperimentStatistic`
        """
        return self._statistic

    @statistic.setter
    def statistic(self, statistic):
        r"""Sets the statistic of this ShowTrainingExperimentDetailsResponse.

        :param statistic: The statistic of this ShowTrainingExperimentDetailsResponse.
        :type statistic: :class:`huaweicloudsdkmodelarts.v1.TrainingExperimentStatistic`
        """
        self._statistic = statistic

    def to_dict(self):
        import warnings
        warnings.warn("ShowTrainingExperimentDetailsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowTrainingExperimentDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
